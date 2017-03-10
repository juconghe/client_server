import socket
import json
import random
from thread import *

def clientThread(sock):
    print("Handling client")
    json_string = sock.recv(1024)
    print("Got the data")
    data = json.loads(json_string)
    OC = data['OC']
    num1 = data['num1']
    num2 = data['num2']
    if not OC in ['+','-','*','/'] or not type(num1) is int or not type(num2) is int:
        # print("Sending data")
        error_msg = json.dumps({'status':300,'value':-1})
        sock.send(error_msg)
    else:
        message = {}
        if OC == '+':
            message = json.dumps({'status':200,'value':num1+num2})
        elif OC == '-':
            message = json.dumps({'status':200,'value':num1-num2})
        elif OC == '*':
            message = json.dumps({'status':200,'value':num1*num2})
        elif num2 == 0:
            message = message = json.dumps({'status':300,'value':-1})
        else:
            message = message = json.dumps({'status':200,'value':num1/num2})
        sock.send(message)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket created")
try:
    s.bind(('localhost',12345))
    s.listen(5)
    while True:
        dropRate = random.randint(0,1)
        (clientsocket,address) = s.accept()
        if dropRate == 0:
            print("connected!")
            start_new_thread(clientThread,(clientsocket,))
        else:
            print("Failed")
            pass
except socket.error as e:
    print(e)
finally:
    s.close()
