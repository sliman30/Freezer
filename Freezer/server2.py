import socket
import re
import os
import ftplib

class Server():
    def __init__ (self, host , port):
        # https://docs.python.org/3/library/socket.html
        self.HOST=host
        self.PORT=port
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(3)

    def wait(self):
        con, addr = self.s.accept()
        print('Connected by', addr)
        self.conn(con,addr)

    def FTP_conn(self):
        ###################################################
        USER   = 'guest'#input("Enter your username : ")
        PASSWD = 'guest'#maskpass.askpass("Enter your password : ")
        HOST   = "10.125.24.63"
        ###################################################
        # Open ftp connection
        self.ftps = ftplib.FTP_TLS(HOST,USER,PASSWD)

    # fonction qui gere 1 client connecté
    def conn(self,con,addr):
        client = True
        data = con.recv(1024).decode()
        print(addr,": ", data)
        print()
        ret=""
        get="ok"
        result =re.search("^([a-z0-9\-@]+) ?([0-9\.A-z\ ]+)?$",data)
        if result.group(1) == "get":
            SONG = result.group(2)
            os.system("spotdl " + SONG + " -p '/home/guest/Music/{title}-{artist}.{ext}'")     
            self.FTP_conn()
            for SONG in os.listdir('/home/imane/Musique'):
                with open(os.path.join('/home/imane/Musique',SONG), 'rb') as file:
                    self.ftps.storbinary(f'STOR {SONG}', file)
        
        msg=""
        for i in get:
            msg+=str(i)+ret

        # on envoie une reponse au client
        con.sendall(msg.encode())
        
serv = Server("10.125.24.56",12002)
serv.wait()