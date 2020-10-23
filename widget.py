#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example, we create a submenu and a menu
separator.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        # Create MenuBar
        menubar = wx.MenuBar()
        
        
        # Create Menu 'File'
        fileMenu = wx.Menu()
        # Create items in Menu 'File'
        newButton  = wx.MenuItem(fileMenu, wx.ID_NEW, '&New\tCtrl+N')
        openButton = wx.MenuItem(fileMenu, wx.wxEVT_ANY, '&Open\tCtrl+O')
        saveButton = wx.MenuItem(fileMenu, wx.wxEVT_ANY, '&Save\tCtrl+S')
        quitButton = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')

        fileMenu.AppendItem(newButton)
        fileMenu.AppendItem(openButton)
        fileMenu.AppendItem(saveButton)
        fileMenu.AppendItem(quitButton)

        # Create Menu 'Import'
        imporT = wx.Menu()
        # Create items in Menu 'Import'
        NewFeed = wx.MenuItem(imporT, wx.wxEVT_ANY, '&NewFeed\tCtrl+F')
        Bookmarks = wx.MenuItem(imporT, wx.wxEVT_ANY, '&Bookmarks\tCtrl+B')
        imporT.AppendItem(NewFeed)
        imporT.AppendItem(Bookmarks)


        # Add Menu 'Import' to Menu 'File'
        fileMenu.AppendMenu(wx.ID_ANY, '&Import', imporT)




        


        self.Bind(wx.EVT_MENU, self.OnQuit, quitButton)
        self.Bind(wx.EVT_MENU, self.OnOpen, openButton)
        self.Bind(wx.EVT_MENU, self.OnSave, saveButton)
        self.Bind(wx.EVT_MENU, self.OnNew, newButton)


        # Add Menu 'Edit' to Menu 'File'
        editMenu = wx.Menu()
        # Create items in Menu 'Edit'
        compileButton = wx.MenuItem(editMenu, wx.wxEVT_ANY, '&Compile\tCtrl+C')
        editMenu.AppendItem(compileButton)



        menubar.Append(fileMenu, '&File')
        menubar.Append(editMenu, '&Edit')

        #self.Bind(wx.EVT_MENU, self.OnCompile, )


        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle('OpenClovis IDE S7')
        self.Centre()

    def OnQuit(self, e):
        self.Close()  
    def OnSave(self, e):
        print 'Saving'   
    def OnOpen(self, e):
        print 'Openning'         
    def OnNew(self, e):
        print 'New'


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()