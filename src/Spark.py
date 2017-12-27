import wx
import ui
import speech_recognition as sr
#from gtts import gTTS
import win32com.client as wincl
#import os
import urllib
import webbrowser
from bs4 import BeautifulSoup
import requests
import re
import wolframalpha
#import playsound
import time
import sys
import winshell
import subprocess
from mutagen.mp3 import MP3

#WolFramAlpha APPID goes here
app_id = 'YT547P-U7GE8G74UV'
speak = wincl.Dispatch('SAPI.SpVoice')
welcome_msg = '''Hello sir, how can I help you?'''

class Gui(ui.MainFrame):
    def __init__(self,parent):
        ui.MainFrame.__init__(self,parent)
        self.display.AppendText(welcome_msg)
        speak.Speak(welcome_msg)

    def SearchFun(self,event):
        try:
            if self.text.GetValue()=='':
                get_audio(False)
            else:
                command(self.text.GetValue())
        except Exception as e:
            print(e)

def play_audio_and_display(text):
    ''' tts = gTTS(text,lang='en')
     _file = text[0:4]+'.mp3'
     tts.save(_file)
     playsound.playsound(_file,True)
     audio = MP3(_file)'''
    frame.display.AppendText('\n'+text+'\n')
    time.sleep(2.5)
    speak.Speak(text)

def wolfram_alpha(query):
    frame.text.SetValue(query)
    frame.display.AppendText('\nSearching on wolframalpha for '+query)
    speak.Speak('Searching on WolFramAlpha for '+query)
    try:
         client = wolframalpha.Client(app_id)
         res = client.query(query)
         ans = next(res.results).text
         play_audio_and_display(ans)
    except:
        #print('Searching on google')
        google(query)

def google(query):
    frame.text.SetValue(query)
    frame.display.AppendText('\nSearching on google for '+query)
    speak.Speak('Searching on google for '+query)
    google_link = 'https://www.google.com/search?q='+query
    html = requests.get(google_link).text
    soup = BeautifulSoup(html, 'lxml')
    tag =  soup.find('span',{'class':'st'})
    url = soup.find('cite').text
    play_audio_and_display(tag.text)
    play_audio_and_display('Would you like to open it in the web browser?')
    audio = ''
    while audio=='':
        audio = get_audio(True)

    if 'yes' in audio.lower():
        webbrowser.open(url)


def wikipedia(query):
    frame.text.SetValue(query)
    frame.display.AppendText('\Searching on wikipedia for '+query)
    speak.Speak('Searching on wikipedia for '+query)
    google_link = 'https://en.wikipedia.org/wiki/'+query
    html = requests.get(google_link).text
    soup = BeautifulSoup(html, 'lxml')
    tags =  soup.find('p')
    #print(tags.text)
    play_audio_and_display(tags.text)

def play_music(music):
     #Search url
    youtube_url = 'https://www.youtube.com/results?search_query='
    #Build a full search url for music request
    youtube_url +=music
    #download a webpage
    html  =  requests.get(youtube_url).text
    #Soupify it
    soup = BeautifulSoup(html, 'lxml')
    #Find all h3 tags
    h3_tags = soup.find_all('h3')
    url =''
    for tag in h3_tags:
        a_tag = tag.find('a')
        if a_tag!= None and a_tag.get('href').startswith('/watch') :
            url = a_tag.get('href')
            break;      #can add more links to list for playlist
    #Build the final link
    url = urllib.parse.urljoin('https://youtube.com/', url)
    webbrowser.open(url)

def dictionary(word):
    url = 'http://www.dictionary.com/browse/'+word
    html = requests.get(url).text
    soup = BeautifulSoup(html,'lxml')
    div_tags =  soup.find_all('div',{'class':'def-content'})

    #If word is mispelled, find the suggested word
    if not div_tags:
        word = soup.find('span',{'class':'me'}).text
        play_audio_and_display('Did you mean '+word+'?')
        url = 'http://www.dictionary.com/browse/'+word
        html = requests.get(url).text
        soup = BeautifulSoup(html,'lxml')
        div_tags =  soup.find_all('div',{'class':'def-content'})


    list = div_tags[0].text.split(':')
    meaning = (list[0]).lstrip()
    sentence = ''
    if len(list)>1:
        sentence = (list[1]).lstrip()
    for tag in div_tags[1:]:
        list = tag.text.split(':')
        if len(list)>1:
            frame.display.AppendText((list[0]).lstrip()+'\nIn sentence: '+(list[1]).lstrip())
            if sentence == '':
                sentence = list[1].lstrip()
    #If no sentence example available
    if sentence:
        play_audio_and_display(meaning +'\nIn sentence: '+sentence)
    else:
        play_audio_and_display(meaning)


def command(request):
    request = request.lower()
    frame.text.SetValue(request)
    if request.startswith('play'):
        play_music(request.replace('play','').lstrip())
    elif re.match('[w,h,i]',request[0:4]):
        wolfram_alpha(request)
    elif 'define' in request:
        dictionary(request.split(' ')[1])
    elif request == 'turn off':
        play_audio_and_display('See you, Niraj!')
        sys.exit()
    elif 'empty' in request:
        try:
            #empty recycle bin
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            self.assertFalse(list(recycle_bin))
            #add empty %temp% files
            time.sleep(5)
            runCommand = 'del /p destination/C:/Users/pnira/AppData/Local/Temp/'
            subprocess.check_call(runCommand)
        except:
            frame.display.AppendText('Something went wrong while deleting the file or recycle bin is already empty')

    elif 'open' in request:
        try:
            os.startfile(request.replace('open','').lstrip()+'.exe')
        except Exception as e:
            frame.display.AppendText(e)
    else:
        google(request)

def get_audio(return_audio):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        frame.display.AppendText('\nListening...\n')
        audio = r.listen(source)

    # Speech recognition using Google API
    try:
        frame.display.AppendText('You said: ' + r.recognize_google(audio)+'\n')
        if return_audio:
            return r.recognize_google(audio)
        else:
            command(r.recognize_google(audio))
    except sr.UnknownValueError:
        frame.display.AppendText('\nGoogle Speech Recognition could not understand audio')
    except sr.RequestError as e:
        frame.display.AppendText('\nCould not request results from Google Speech Recognition service; {0}'.format(e))


if __name__ == '__main__':
    app =  wx.App(False)
    frame = Gui(None)
    frame.Show(True)
    app.MainLoop()
