import os
import json
import base64
from glob import glob

class FileInterface:
    
    def __init__(self):
        os.chdir('files/')

    def list(self):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,filename=''):
        if(filename==''):
            return None
        try:
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))
    
    def delete(self,filename=''):
        if(filename==''):
            return None
        try:
            os.remove(f"{filename}")
            return dict(status='OK',data=f"{filename} berhasil di hapus")
        except Exception as e:
            return dict(status='ERROR',data=str(e))
    
    def upload(self,filename='', filecontent=''):
        if (filename=='' or filecontent==''):
            return None
        try:
            fp = open(filename,'wb+')
            filecontent_decoded = base64.b64decode(filecontent)
            fp.write(filecontent_decoded)
            fp.close()
            return dict(status='OK', data=f"{filename} berhasil di upload")
        except Exception as e:
            return dict(status='ERROR',data=str(e))

if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get('pokijan.jpg'))
    print(f.delete('pokijan.jpg'))
    print(f.upload('pokijan.jpg'))
