import socket
import json

d = 0.1
try:
    while True:
        if d > 2:
            raise Exception('Time out is over 2')
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(d)
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
            d = 0.1
            if status != 200:
                print("The input is not valid, either operation not support or number is not integer")
            else:
                print(value)
            s.close()
            d *= 2.0
        except Exception as e:
            if e is KeyboardInterrupt:
                break
            else:
                d *= 2.0
                print("Timeout!")
                print("Value of time out is: {}".format(d))
                continue
except socket.error as e:
    print(e)
