import zmq
import signal

signal.signal(signal.SIGINT, 0)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Listening on port 5555")

while True:
    #  Wait for next request from client
    message = socket.recv_string()
    print(f"Received request: {message}")
    socket.send(f"Ack: {message}")