#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example we use automatic ids
with wx.ID_ANY.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        panel = wx.Panel(self)
        grid = wx.GridBagSizer(1, 1)
        self.exitButton = wx.Button(panel, 100, 'Exit')
        grid.Add(self.exitButton, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=30)


        self.CGV = wx.Button(panel, 1342, 'CGV')
        grid.Add(self.CGV, pos=(0,2), flag=wx.RIGHT|wx.TOP, border=30)



        self.Bind(wx.EVT_BUTTON, self.Handler, id=self.exitButton.GetId())
        self.Bind(wx.EVT_BUTTON, self.Handler, id=self.CGV.GetId())

        self.SetTitle("Automatic ids")
        self.Centre()

        panel.SetSizer(grid)
        grid.Fit(self)

    def Handler(self, event):
        if event.GetId() == self.exitButton.GetId():
            self.Close()
        elif event.GetId() == self.CGV.GetId():
            print 'CGV button'


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()