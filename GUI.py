import wx
import sys, os
import wx.lib.agw.multidirdialog as MDD
import time
from string import digits 
import re
import string

wildcard = "Python source (*.txt)|*.txt|" \
            "All files (*.*)|*.*"
upload_file_path = ''
uploadfile_text = ''
class MyFrame(wx.Frame):   
     
    def __init__(self):
        super().__init__(parent=None, title='TEXT CLEANER GUI', size =(510,200) ,style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self,size=(800, 50), pos=(0, 0), style=wx.SIMPLE_BORDER)
        self.bSizer = wx.BoxSizer(wx.VERTICAL)
        self.bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.Go_btn = wx.Button(self.panel, label='CLean Text', pos=(110, 10),style=wx.NO_BORDER)
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.Go_btn.SetFont(font)
        self.Go_btn.Bind(wx.EVT_BUTTON, self.GO_btn)
        self.Go_btn.SetForegroundColour('Black')
        self.Go_btn.SetBackgroundColour('Green')

        self.Exit_btn = wx.Button(self.panel, label='EXIT', pos=(200, 10),style=wx.NO_BORDER)
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.Exit_btn.SetFont(font)
        self.Exit_btn.Bind(wx.EVT_BUTTON, self.exit)
        self.Exit_btn.SetForegroundColour('White')
        self.Exit_btn.SetBackgroundColour('Red')

        self.openFileDlgBtn = wx.Button(self.panel, label="Upload File", pos=(20, 10),style=wx.NO_BORDER)
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.openFileDlgBtn.SetForegroundColour('black')
        self.openFileDlgBtn.SetBackgroundColour('#0dfcdb')
        self.openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)

        self.bSizer.Add(self.openFileDlgBtn, 0, wx.ALL|wx.CENTER, 5)

        font1 = wx.Font(16, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.Upd_text = wx.StaticText(self.panel,-1, label = "Total Uploded Text Found :  ",pos=(20, 69))
        self.Upd_text.SetForegroundColour('Black')
        self.Upd_text.SetFont(font1)
        self.Upd_text.Hide()

        self.Stopwords = wx.StaticText(self.panel,-1, label = "Total Stopwords Text :  ",pos=(20, 95))
        self.Stopwords.SetForegroundColour('Black')
        self.Stopwords.SetFont(font1)
        self.Stopwords.Hide()

        with open("C:\\text cleaner app\\stopwords.txt" , "r") as f1:
            stopwords = f1.readlines()
            self.Stopwords.SetLabel(f'Total Stopwords Text :  {str(len(stopwords))}')
            self.Stopwords.SetForegroundColour('Black')
        # self.process_lbl = wx.StaticText(self.panel,-1,label = "Total Cleaned Text: ",pos=(20, 120),style = wx.ALIGN_CENTER)
        # self.process_lbl.SetFont(font1)
        # self.process_lbl.Hide()
        self.count = 0
        self.Show()    
    def GO_btn(self,event):
        if upload_file_path == '':
            wx.MessageBox(' -_- Please Upload File  -_- ', 'TEXT CLEANER GUI',wx.OK | wx.ICON_ERROR)
        else:
            self.Destroy()

    def exit(self,event):
        dlg = wx.MessageDialog(None, "Stop Process And Exit !!!", 'TEXT CLEANER GUI', wx.YES_NO | wx.ICON_WARNING)
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            self.Destroy()
            sys.exit()
        else:
            pass
    
    def onOpenFile(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file",defaultDir='', defaultFile="",wildcard=wildcard,style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print("You chose the following file(s):")
            for path in paths:
                global upload_file_path 
                upload_file_path = str(path)
                print(path)
            with open(upload_file_path,encoding='utf-8') as f:
                doc = f.readlines()
                global uploadfile_text 
                uploadfile_text = str(len(doc))
                self.Upd_text.Show()
                self.Upd_text.SetLabel(f'Total Uploded Text Found:  {uploadfile_text}')
                self.Upd_text.SetForegroundColour('Black')
                self.Stopwords.Show()
                # self.gauge = wx.Gauge(self.panel, range = len(doc), size = (400, 25) , pos=(20, 40), style = wx.GA_HORIZONTAL)
                
        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    # frame = MyFrame1()
    frame = MyFrame()
    app.MainLoop()

import Text_cleaner_code
Text_cleaner_code.code(upload_file_path,uploadfile_text)