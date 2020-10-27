#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example, we create two horizontal
toolbars.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


EVT_TRUMP = 2
EVT_BIDEN = 3


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        # Create a vertical box
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Create sketon of toolbar
        self.toolbar = wx.ToolBar(self)
        # Create two buttons in toolbar
        trumpButton = self.toolbar.AddTool(EVT_TRUMP, wx.Bitmap('Trump.jpg'))
        bidenButton = self.toolbar.AddTool(EVT_BIDEN, wx.Bitmap('Biden.jpg'))

        # Enable two buttons
        self.toolbar.EnableTool(EVT_BIDEN, True)
        self.toolbar.EnableTool(EVT_TRUMP, True)

        # Add seperators
        self.toolbar.AddSeparator()
        self.toolbar.AddSeparator()
        texit = self.toolbar.AddTool(wx.ID_EXIT, wx.Bitmap('Biden.jpg'))
        # Active toolbar
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, texit)
        self.Bind(wx.EVT_TOOL, self.OnSelectTrump, trumpButton)
        self.Bind(wx.EVT_TOOL, self.OnSelectBiden, bidenButton)

        # Add toolbar to vbox so we can fix the size
        vbox.Add(self.toolbar, 0, wx.EXPAND)
        self.SetSizer(vbox)
        
        self.SetSize((350, 250))
        self.SetTitle('Undo redo')
        self.Centre()



    def OnSelectTrump(self, e):
        self.toolbar.EnableTool(EVT_BIDEN, True)
        self.toolbar.EnableTool(EVT_TRUMP, False)

    def OnSelectBiden(self, e):
        self.toolbar.EnableTool(EVT_BIDEN, False)
        self.toolbar.EnableTool(EVT_TRUMP, True)

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()