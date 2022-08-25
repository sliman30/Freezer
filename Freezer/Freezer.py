from multiprocessing.dummy.connection import Client
from zipapp import get_interpreter
import maskpass
import ftplib
import os
import playsound
import shutil
import client

class MyFTP():
    def __init__(self):
        self.flag = 0
        self.dirFTP = "/home/imane/Musique/"
        self.Songs = []

    def FTP_conn(self):
        # Open ftp connection
        USER   = 'guest'#input("Enter your username : ")
        PASSWD = 'guest'#maskpass.askpass("Enter your password : ")
        HOST   = "10.125.24.56"
        self.ftps = ftplib.FTP_TLS(HOST,USER,PASSWD)

    def FTP_UPdatelist(self):
        self.FTP_conn()
        # List The Distant Music Directory
        try:
            self.Songs = self.ftps.nlst()
        except ftplib.error_perm as resp:
            if str(resp) == "550 No files found":
                print("No Songs in this directory")
            else:
                raise

    def FTP_list(self):
        for s in Ftp.Songs:
            print(s)
            
    def FTP_GetLocally(self):
        for f in self.Songs:
            if SONG in f:
                print('Song exists')
                localfile = open(f, 'wb')        
                self.ftps.retrbinary('RETR ' + f, localfile.write, 1024)
                self.Song_name = str(localfile).split("'")[1]
                self.Song_path = os.path.abspath(str(self.Song_name))
                try:
                    shutil.move(self.Song_path,self.dirFTP)
                except:
                    pass
                self.flag = 1
    
    def FTP_Get(self):
        for f in self.Songs:
            localfile = open(f, 'wb')        
            self.ftps.retrbinary('RETR ' + f, localfile.write, 1024)
            self.Song_name = str(localfile).split("'")[1]
            self.Song_path = os.path.abspath(str(self.Song_name))
            if self.Song_name in f:
                try:
                    shutil.move(self.Song_path,self.dirFTP)
                except:
                    pass
                self.flag = 1

###################################################
Ftp = MyFTP()
Ftp.FTP_UPdatelist()
Ftp.FTP_list()

SONG = input("What song w'd you like to listen to ? ")
Ftp.FTP_GetLocally()

###################################################

if Ftp.flag == 1:
    Ans = input('Do you want to play it ? ')
    if Ans == 'yes':
        Song_path2 = Ftp.dirFTP+Ftp.Song_name
        playsound.playsound(Song_path2)
else:
    print('Song does not exist in your Library. Download started')    
    ClientLocal = client.Client()
    ClientLocal.connect("get "+ SONG)
    ClientLocal.close()
    Ftp.FTP_UPdatelist()
    Ftp.FTP_Get()