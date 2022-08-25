from multiprocessing.dummy.connection import Client
from zipapp import get_interpreter
import maskpass
import ftplib
import os
import playsound
import shutil
import socket
import client2

###################################################
USER   = 'guest'#input("Enter your username : ")
PASSWD = 'guest'#maskpass.askpass("Enter your password : ")
HOST   = "10.125.24.84"
###################################################
# Open ftp connection

ftps = ftplib.FTP_TLS(HOST,USER,PASSWD)
###################################################
# List The Distant Music Directory
try:
    Songs = ftps.nlst()
except ftplib.error_perm as resp:
    if str(resp) == "550 No files found":
        print("No Songs in this directory")
    else:
        raise

for s in Songs:
    print(s)
###################################################
# 
dirFTP = "/home/imane/Musique/"
SONG = input("What song w'd you like to listen to ? ")
flag = 0
for f in Songs:
    if SONG in f:
        print('Song exists')
        localfile = open(f, 'wb')        
        ftps.retrbinary('RETR ' + f, localfile.write, 1024)
        Song_name = str(localfile).split("'")[1]
        Song_path = os.path.abspath(str(Song_name))
        shutil.move(Song_path,dirFTP)
        flag = 1
###################################################

if flag == 1:
    Ans = input('Do you want to play it ? ')
    if Ans == 'yes':
        Song_path2 = dirFTP+Song_name
        playsound.playsound(Song_path2)
else:
    print('Song does not exist in your Library. Download started')
    
    ClientLocal = client2.Client()
    ClientLocal.connect("get "+ SONG)
    localfile = open(f, 'wb')        
    ftps.retrbinary('RETR ' + f, localfile.write, 1024)
    Song_name = str(localfile).split("'")[1]
    Song_path = os.path.abspath(str(Song_name))
    shutil.move(Song_path,dirFTP)
    ClientLocal.close()
    #os.system("spotdl " + SONG + " -p '~/Musique/{title}-{artist}.{ext}'")
    # for SONG in os.listdir(dirFTP):
    #     with open(os.path.join(dirFTP,SONG), 'rb') as file:
    #         ftps.storbinary(f'STOR {SONG}', file)
