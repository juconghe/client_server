import socket
import json

try:
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('localhost',12345))
        # print("connected to the server")
        OC = raw_input('Enter the OC: ')
        num1 = input('Enter the first number: ')
        num2 = input('Enter the second number: ')
        s.send(json.dumps({'OC':OC,'num1':num1,'num2':num2}))
        message = s.recv(1024)
        data = json.loads(message)
        status = data['status']
        value = data['value']
        if status != 200:
            print("The input is not valid, either operation not support or number is not integer")
        else:
            print(value)
        s.close()
except socket.error as e:
    print(e)
