import socket
import json
from thread import *

def clientThread(sock):
    # print("Handling client")
    # waiting for client to send message
    json_string = sock.recv(1024)
    # print("Got the data")
    #pase json
    data = json.loads(json_string)
    OC = data['OC']
    num1 = data['num1']
    num2 = data['num2']
    #check OC and num1 and num2
    if not OC in ['+','-','*','/'] or not type(num1) is int or not type(num2) is int:
        # print("Sending data")
        # send error message back to the server with status code 300 and value -1
        error_msg = json.dumps({'status':300,'value':-1})
        sock.send(error_msg)
    else:
        message = {}
        #handle opeartion
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
        # send message to client in JSON formate
        sock.send(message)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket created")
try:
    #open server at address localhost with port 12345
    s.bind(('localhost',12345))
    # set max clients to 5
    s.listen(5)
    while True:
        # waiting for client to connected
        (clientsocket,address) = s.accept()
        print("connected!")
        # Hand the client in new thread
        start_new_thread(clientThread,(clientsocket,))
except socket.error as e:
    print(e)
finally:
    s.close()
