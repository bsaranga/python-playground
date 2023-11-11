import threading
import zmq
import os
import signal

signal.signal(signal.SIGINT, 0)

print(f"PID: {os.getpid()}")
print("Listening on port 5555")


def worker_routine(worker_url: str,
                   context: zmq.Context = None):
    """Worker routine"""
    context = context or zmq.Context.instance()

    # Socket to talk to dispatcher
    socket = context.socket(zmq.REP)
    socket.connect(worker_url)

    while True:
        message = socket.recv_string()
        print(f"Received request: [ {message} ]")

        # Send reply back to client
        socket.send_string(f"Ack: {message}")


def main():
    """Server routine"""

    url_worker = "inproc://workers"
    url_client = "tcp://*:5555"

    # Prepare our context and sockets
    context = zmq.Context.instance()

    # Socket to talk to clients
    clients = context.socket(zmq.ROUTER)
    clients.bind(url_client)

    # Socket to talk to workers
    workers = context.socket(zmq.DEALER)
    workers.bind(url_worker)

    # Launch pool of worker threads
    for i in range(5):
        thread = threading.Thread(target=worker_routine, args=(url_worker,))
        thread.daemon = True
        thread.start()

    zmq.proxy(clients, workers)

    # We never get here but clean up anyhow
    clients.close()
    workers.close()
    context.term()


if __name__ == "__main__":
    main()