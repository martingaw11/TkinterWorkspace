import socket

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 8049))

    def send_message(self, message):
        message += '\n'
        self.client_socket.sendall(message.encode('utf-8'))
        data = self.client_socket.recv(1024)
        print('Received', repr(data.decode('utf-8')))

    def close(self):
        self.client_socket.close()

# main function
if __name__ == '__main__':
    client = Client()

    # Sending a message to the server
    client.send_message("Hello from the client!")

    client.close()
