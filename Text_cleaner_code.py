import wx
import sys, os
import time
from string import digits 
import re
import string
app = wx.App()
def code(upload_file_path,uploadfile_text):
    upload_file_path = upload_file_path.replace('\\','\\\\')
    try:
        with open(upload_file_path,encoding='utf-8') as f:
            doc = f.readlines()
            print('Uploaded File Text: Processing...........')
            doc = [d.replace("\n", " ") for d in doc]
            doc = [re.sub(r'[!"#$%&()*,-./:;<=>?@[\]^_`{|}~]', ' ', d) for d in doc ]
            doc = [d.translate(str.maketrans(' ', ' ', digits)) for d in doc]
            print('Uploaded File Text: Done')
            f.close()

        with open("C:\\text cleaner app\\stopwords.txt" ,encoding='utf-8') as f1:
            stopwords = f1.readlines()
            print('StopWord : Processing...........')
            stopwords_Arr = []
            for s in stopwords:
                sword = s.lower().strip()
                sword1 = f' {sword} '
                sword2 = f'{sword} '
                sword3 = f' {sword}'
                sword4 = f'{sword}' 
                stopwords_Arr.append(sword1)
                stopwords_Arr.append(sword2)
                stopwords_Arr.append(sword3)
                stopwords_Arr.append(sword4)
            print('StopWord : Done')
            f1.close()

        with open("C:\\text cleaner app\\Cleaned Text.txt" , "w") as f2:
            print('Cleaned Text : Processing...........')
            count = 0
            # clean_text_list = []
            for d in doc:
                d = [word for word in d.split() if word.lower() not in stopwords_Arr ]
                d = " ".join(d)
                d = re.sub(r'No', "", d)
                d = re.sub('\s+', ' ', d)
                if d != '':
                    f2.write(str(d)+'\n')
                count += 1
                print(f'Cleaned Text {str(count)} / {str(uploadfile_text)} : {str(d)} ') 
            f2.close()
            print('Cleaned Text : Done')
            wx.MessageBox(' -_- ALL PROCESS DONE  -_- ', 'TEXT CLEANER GUI',wx.OK | wx.ICON_INFORMATION)
            sys.exit()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print("Error ON : ", sys._getframe().f_code.co_name + "--> " + str(e), "\n", exc_type, "\n", fname, "\n",exc_tb.tb_lineno)
        wx.MessageBox(' -_- Error on Text Cleaner App -_- ', 'TEXT CLEANER GUI',wx.OK | wx.ICON_INFORMATION)