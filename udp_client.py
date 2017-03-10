import socket
import json


# initial the delay to 0.1
d = 0.1
failed = False
OC = ''
num1 = 0
num2 = 0
try:
    # keep the client running until user interrupt
    while True:
        # if the server didn't reply back the message or time out, allow user to input new task
        # otherwise skip this step and send the server with old task
        if not failed:
            OC = raw_input('Enter the OC: ')
            num1 = input('Enter the first number: ')
            num2 = input('Enter the second number: ')
        try:
            if d > 2:
                # raise excpetion tell the user time out is reach 2
                raise Exception('Time out is over 2')
            # create a socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # set time out
            s.settimeout(d)
            # connect to the server
            s.connect(('localhost',12345))
            # print("connected to the server")
            # send message in JSON format
            s.send(json.dumps({'OC':OC,'num1':num1,'num2':num2}))
            # wait for message to reply from the server
            message = s.recv(1024)
            # parse the JSON
            data = json.loads(message)
            status = data['status']
            value = data['value']
            # the the time out back to 0.1
            d = 0.1
            # if the status indicate not 200, it implies the input is not correct, warn the user
            if status != 200:
                print("The input is not valid, either operation not support or number is not integer")
            else:
                # tell the user the result
                print("The result is: {}".format(value))
                # close the socket
            s.close()
            # change faild to false indicate user can input new task
            failed = False
        except Exception as e:
            # handle the case user wanna quit the clinet manully
            if e is KeyboardInterrupt:
                break
            else:
                # indicate time out reach 2, abort task and let user start new task
                if d < 2:
                    d *= 2.0
                    failed = True
                else:
                    # still within timeout range, retrying send the message to the server
                    d = 0.1
                    failed = False
                    print("Timeout!")
                # print("Value of time out is: {}".format(d))
                continue
except socket.error as e:
    print(e)
