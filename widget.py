import wx
import sys

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,"Popup Menu Example")
        
        self.window = wx.Window(self)

        # Create menu 'File'
        fileMenu = wx.Menu()

        # Create exit and open button
        exitButton = wx.MenuItem(fileMenu, -1, '&Exit\tCtrl+X')
        openButton = wx.MenuItem(fileMenu, -1, '&Open File\tCtrl+O')

        # Add two buttons into menu 'File'
        fileMenu.AppendItem(exitButton)
        fileMenu.AppendItem(openButton)

        # Bind Exit button to OnExit handler
        self.Bind(wx.EVT_MENU, self.OnExit, exitButton)


        # Create MenuBar          
        menuBar = wx.MenuBar()
        # Add menu 'File' to 'Menu'
        menuBar.Append(fileMenu, "Menu")
        self.SetMenuBar(menuBar)


        wx.StaticText(self.window, wx.ID_ANY,"Right-click on the panel to show a popup menu", (25, 70))

        # Create a popupmenu appeared once user click right-click.
        self.popupmenu = wx.Menu()

        # Create two items
        exitButtonPop = wx.MenuItem(self.popupmenu, -1, '&Exit\tCtrl+X')
        openButtonPop = wx.MenuItem(self.popupmenu, -1, '&Open File\tCtrl+O')

        # Bind Exit button to OnExitPop handler
        self.Bind(wx.EVT_MENU, self.OnExitPop, exitButtonPop)

        # Bind Open button to OnOpenPop handler
        self.Bind(wx.EVT_MENU, self.OnOpenPop, openButtonPop)

        # Add Exit and Open button into popup menu
        item = self.popupmenu.AppendItem(exitButtonPop)
        item = self.popupmenu.AppendItem(openButtonPop)

        # Bind right-click event to OnShowPopup handler
        self.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup)


    def OnShowPopup(self, event):
        # Once righ-click, it is triggerd
        currentMosePosition = event.GetPosition()
        currentMosePosition = self.window.ScreenToClient(currentMosePosition)
        self.window.PopupMenu(self.popupmenu, currentMosePosition)
        

    def OnPopupItemSelected(self, event):
        print 'widget[%d]: event = %s'%(sys._getframe().f_lineno, event.GetId())
        item = self.popupmenu.FindItemById(event.GetId())
        text = item.GetText()

        wx.MessageBox("You selected item '%s'" % text, style=wx.ICON_WARNING)
        

    def OnExit(self, event):
        print 'Exiting'

    def OnExitPop(self, event):
        print 'Exiting'

    def OnOpenPop(self, event):
        print 'Opening'    
        

app = wx.PySimpleApp()
frame = MyFrame()
frame.Show()
app.MainLoop()