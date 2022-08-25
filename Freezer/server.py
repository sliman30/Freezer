import socket
import re
import os

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
        
        msg=""
        for i in get:
            msg+=str(i)+ret

        # on envoie une reponse au client
        con.sendall(msg.encode())
        con.close()
        self.s.close()
        
serv = Server("10.125.24.56",12002)
serv.wait()
serv.s.close()