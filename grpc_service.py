import grpc
import chat_pb2

def send_messages(stub):
    requests = [
        chat_pb2.MessageRequest(content="Hello from Python"),
        chat_pb2.MessageRequest(content="How are you?"),
        chat_pb2.MessageRequest(content="Goodbye!")
    ]

    # Send messages to the server
    for request in requests:
        stub.SendMessage(request)

    # Receive responses from the server
    for response in stub.SendMessage(iter(requests)):
        print(f"Received response: {response.content}")


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatStub(channel)
    send_messages(stub)


if __name__ == '__main__':
    run()
