import socket

class Client:

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 8049))

    def send_command(self, command):
        command += '\n'
        self.client_socket.sendall(command.encode('utf-8'))
        data = self.client_socket.recv(1024)
        print('Received', repr(data.decode('utf-8').rstrip()))

    def write_command(self):
        while True:
            message = input("Enter message to send: ")
            message += '\n'
            self.client_socket.sendall(message.encode('utf-8'))
            data = self.client_socket.recv(1024)
            print('Server: ', repr(data.decode('utf-8').rstrip()))
            if message == "exit\n":
                break
        

    def close(self): 
        self.client_socket.close()

# main function
if __name__ == '__main__':
    client = Client()

    #client.send_command("Brakes: On")

    client.write_command()

    client.close()