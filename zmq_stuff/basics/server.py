#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Listening on port 5555")

try:
    while True:
        #  Wait for next request from client
        message = socket.recv_string()
        print("Received request: %s" % message)
        socket.send(b"World")

except KeyboardInterrupt:
    print("Server terminated")
    socket.close()
    context.term()