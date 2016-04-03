# Python server/client project using python version 3.3
print ("********   Networking (Client Side)   *********\n".upper())



import socket               # Import socket module
import sys
import threading

class NewThread(threading.Thread):
    def __init__(self, target, *args):
        threading.Thread.__init__(self)
        self._target = target
        self._args = args
 
    def run(self):
        self._target(*self._args)

def Recv():
    while True:
        data = s.recv(BUFFER_SIZE)
        data = data.decode(encoding='UTF-8',errors='strict')
        print('\n' + data)

def mySend(data):
    try:
        s.sendto(bytes(data + "\n", 'utf-8'), (IP, UDP_PORT))
    except socket.error:
        print('connection error')

def fileListener(Port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', Port))
    sock.listen(1)
    conn, addr = s.accept()
    print ('Connecting for file...')
    f = open("TEST.txt",'wb') #open in binary
    l=1
    while(l):
        l = sock.recv(BUFFER_SIZE)
        while(l):
            f.write(l)
            l = sc.recv(1024)
        print('File transfer complete...')
        f.close()
    conn.close()
    sock.close()

def fileSender(FileName, Port):
    s = socket.socket()
    s.connect(("127.0.0.1", Port))
    print('Connected for file transfer...')
    f = open(FileName, "rb")
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    print('File transfer complete...')
    s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         # Create a socket object
IP = '127.0.0.1'
UDP_PORT = 5050
BUFFER_SIZE = 1024
x = 0

mySend("[START]")                                           # Initialize the port by sending data to the server
RecvThread = NewThread(Recv)
RecvThread.start()

username = input("Please enter a username: ")
sendstr = "[USER] " + username
mySend(sendstr) 

while True:
    message = input("> ")
    sendstr = "[MSSG] " + message
    mySend(sendstr) 
