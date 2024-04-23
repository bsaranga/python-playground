import os
import zmq
import signal
import time

signal.signal(signal.SIGINT, 0)

print(f"PID: {os.getpid()}")
print("Bound to port 5555")

with zmq.Context() as context:
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    response = context.socket(zmq.REP)

    publisher.bind("tcp://*:5555")
    response.bind("tcp://*:5556")

    for i in range(0, 5, 1):
        publisher.send_string(f"warm-up: {i}")
        time.sleep(0.1)

    while True:
        request = response.recv_string()
        if (request == "requesting stream..."):
            response.send_string(f"Ack")
            time.sleep(2)
            for i in range(0, 5, 1):
                publisher.send_string(f"HELLO WORLD >{i}>")
            