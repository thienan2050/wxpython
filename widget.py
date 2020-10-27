#!/usr/bin/python

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        # Create a skeleton for ToolBar
        toolbar = self.CreateToolBar()

        # Create two icon
        self.Trump = wx.Bitmap("Trump.jpg")
        self.Biden = wx.Bitmap("Biden.jpg")

        # Add icons to ToolBar
        toolbar1 = toolbar.AddTool(-1,self.Trump)
        toolbar2 = toolbar.AddTool(-1,self.Biden)

        # Active them
        toolbar.Realize()

        #Bind them to their handler
        self.Bind(wx.EVT_TOOL, self.OnSelectTrump, toolbar1)
        self.Bind(wx.EVT_TOOL, self.OnSelectBiden, toolbar2)

        # Set size
        self.SetSize((350, 250))
        # Set title
        self.SetTitle('Vote Vote Vote !!!')
        # Set center
        self.Centre()

    def OnSelectTrump(self, e):
        print ('You have selected Trump as President')

    def OnSelectBiden(self, e):
        print ('You have selected Biden as President')


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
