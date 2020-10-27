#!/usr/bin/python

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        #Create a vertical box
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Create a skeleton for ToolBar1
        toolbar1 = wx.ToolBar(self)


        # Create two icon
        self.Trump = wx.Bitmap("Trump.jpg")
        self.Biden = wx.Bitmap("Biden.jpg")

        # Add icons to ToolBar
        icon1 = toolbar1.AddTool(-1,self.Trump)
        icon2 = toolbar1.AddTool(-1,self.Biden)

        # Active them
        toolbar1.Realize()


        # Create a skeleton for ToolBar2
        toolbar2 = wx.ToolBar(self)

        icon4 = toolbar2.AddTool(-1, self.Biden)
        icon3 = toolbar2.AddTool(-1, self.Trump)
        

        toolbar2.Realize()


        # Add two toolbar to vertical box
        vbox. (toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar2, 0, wx.EXPAND)
        
        self.SetSizer(vbox)

        #Bind them to their handler
        self.Bind(wx.EVT_TOOL, self.OnSelectTrump, icon1)
        self.Bind(wx.EVT_TOOL, self.OnSelectBiden, icon2)
        self.Bind(wx.EVT_TOOL, self.OnSelectTrump, icon3)
        self.Bind(wx.EVT_TOOL, self.OnSelectBiden, icon4)

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
