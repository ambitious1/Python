# Python server/client project using python version 3.3
print ("*********  networking (SERVER SIDE)  **********\n\n.".upper())

#import socket               # Import socket module
import threading
import socketserver
import ctypes

class ClientThread(threading.Thread):
    def __init__(self, target, *args):
        threading.Thread.__init__(self)
        self._target = target
        self._args = args
 
    def run(self):
        self._target(*self._args)

class Client:
    def __getitem__(self,key):
        return self.User

    def __init__(self):
        self.s = 0
        self.thread = 0
        self.bAlive = False
        self.nSent = 0
        self.nRecv = 0
        self.username = ''
        self.data = 0

    def new(self):
        self.s = 0
        self.thread = 0
        self.bAlive = True
        self.nSent = 0
        self.nRecv = 0
        self.username = ''
        self.data = 0

    def mysend(self, msg):
        totalsent = 0
        while totalsent < BUFFER_SIZE:
            sent = User.s.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

def NewClient(UserList, IP):
    lock.acquire()
    try:
        for x in range(0, 19):
            if UserList[x].bAlive == False:
                UserList[x].new()
                break
    finally:
        lock.release()
    return UserList[x]

def setUser(User):
    User.username = User.data[11:]
    sendstr = "Username set: " + User.username
    User.s.request[1].sendto(bytes(sendstr, 'utf-8'), User.s.client_address)

def processMessage():
    User.data = User.data[7:]
    User.s.send(bytes(User.data, 'utf-8'))

def ClientFunc(User):
    print ('Thread started')
    try:
        data = User.s.request[0].strip()
    except: return
    if not data: return
    print ('Received data: ', data)
    User.data = data.decode('utf-8')
    User.data = User.data.lower()
    if "[username]" in User.data: setUser(User)
    elif "[mssg]" in User.data and User.username is not '': processMessage()
    print ('End of connection: ', User.s.client_address)

class RequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print ('\nConnection received: ', self.client_address[0])
        User = NewClient(UserList, self.client_address[0])
        User.address = self.client_address
        User.s = self
        User.thread = ClientThread(ClientFunc, User)
        User.thread.start()
        return

class ForkingServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

IP = '127.0.0.1'
UDP_PORT = 5050
BUFFER_SIZE = 255
UserList = []
for x in range(0, 19):
    UserList.append(Client())
lock = threading.Lock()

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ForkingServer((IP, UDP_PORT), RequestHandler)         # Create a socket object
t = threading.Thread(target=s.serve_forever)
t.setDaemon(True) # don't hang on exit
t.start()
