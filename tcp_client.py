import socket
import json

try:
    while True:
        # create a socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # connect to the server
        s.connect(('127.0.0.1',12345))
        # print("connected to the server")
        # accept input
        OC = raw_input('Enter the OC: ')
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        # send message to the server in JSON format
        s.send(json.dumps({'OC':OC,'num1':num1,'num2':num2}))
        #wait for reply
        message = s.recv(1024)
        # pass JSON
        data = json.loads(message)
        status = data['status']
        value = data['value']
        #out put the result
        if status != 200:
            print("The input is not valid, either operation not support or number is not integer")
        else:
            print(value)
        s.close()
except socket.error as e:
    print(e)
