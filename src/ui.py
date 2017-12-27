import wx
import wx.xrc

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer3.SetMinSize( wx.Size( 100,100 ) )

		bSizer3.Add( ( 0, 0), 1, 0, 1 )

		self.text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 750,-1 ), 0|wx.NO_BORDER )
		self.text.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.text.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.text.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer3.Add( self.text, 0, wx.ALIGN_CENTER, 5 )

		self.search = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )
		self.search.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.search.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer3.Add( self.search, 0, wx.ALIGN_CENTER, 10 )


		bSizer3.Add( ( 0, 0), 1, 0, 1 )


		bSizer3.Add( ( 0, 0), 1, 0, 0 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.display = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,400 ), wx.TE_AUTO_URL|wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP|wx.ALWAYS_SHOW_SB|wx.VSCROLL )
		self.display.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cambria" ) )

		bSizer5.Add( self.display, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.text.Bind( wx.EVT_TEXT_ENTER, self.SearchFun )
		self.search.Bind( wx.EVT_BUTTON, self.SearchFun )
		self.search.Bind( wx.EVT_LEFT_DCLICK, self.SearchFun )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SearchFun( self, event ):
		event.Skip()
