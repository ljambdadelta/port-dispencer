import socket

class mClient:
    def __init__(self, boss, boss_port):
        self.boss = boss
        self.boss_port = boss_port
        self.i_am =socket.gethostname() 
        self.connection = None

    def connect(self):
        self.connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.boss)
        print(self.boss_port)
        self.connection.connect((self.boss, self.boss_port))
        payload=("REG "+ self.i_am)
        self.connection.sendall(str.encode(payload))
        

    def read_answer(self):
        return self.connection.recv(1024)   

    def give_azport(self):
        self.connect()
        port_from_db = int(self.read_answer().decode())
        print(port_from_db)
        if (port_from_db < 0) is True:
            return -1
        return port_from_db

    
    def do_it_dirty(self):
        self.connect()
        return 
