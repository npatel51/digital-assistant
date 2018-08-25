# Synopsis
Spark: A search bot that takes _text_ or _voice_ as an input and responds in form of text and audio. It can play music from YouTube, delete temporary files on your computer, open programs available in OS, perform Mathematical calculations, shutdown itself, and more. 

# Features
Spark could do the following ( you can either type in the search box or click on the search button to initiate):
  * Play music on YouTube (e.g. Say or type 'play song you like')
  * Mathematical calculation 
  * Basic Search ( Say 'what is github?') 
  * Delete temporary files, empty recycle bin
  * Find a definition and example sentence ( Say 'define propine')
  * Displays the result on GUI
  * Open programs (Say something like 'open Excel')
  * Turn's off (Say 'Turn off')
  * More coming soon 
  
# Installation

Clone and Install the requirements.

    cd ~
    git clone https://github.com/npatel51/Spark.git
    cd Spark\src\
    pip install -r requirements.txt
    
For standalone executable install [PyInstalller](https://pythonhosted.org/PyInstaller/)

For Windows, PyWin32 or the more recent [pypiwin32](https://pypi.org/project/pypiwin32/) is a prerequisite.
    
    pip install pypiwin32
    pip install pyinstaller
    Go to the program directory
    cd Spark\src\
    pyinstaller Spark.py
    cd Spark\dist\Spark\Spark.exe
  
It will generate a bundle in the directory called dist where you could find the executable file. I've chosen Wolfram Alpha as primary search place for any query if you do decide to use it you would need a Wolfram [AppID](https://developer.wolframalpha.com/portal/signup.html) to call the Wolfram Alpha API.

# Demo
![](https://github.com/npatel51/Spark/blob/master/Images/play_song.gif)


![](https://github.com/npatel51/Spark/blob/master/Images/Search.JPG)







 
