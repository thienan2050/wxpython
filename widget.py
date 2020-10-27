#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we place a panel inside 
another panel.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)

        panel.SetBackgroundColour('#a539d1')
        vbox = wx.BoxSizer(wx.VERTICAL)
        

        midPan = wx.Panel(panel)
        midPan.SetBackgroundColour('#2a752e')

        vbox.Add(midPan, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(vbox)


def main():

    app = wx.App()
    ex = Example(None, title='Border')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()



 
