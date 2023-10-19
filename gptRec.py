import socket

if __name__ == '__main__':
    HOST = 'localhost'  # The server's hostname or IP address
    PORT = 8049         # The port used by the server

    message = input("Enter message to send: ").strip()
    print()

    while message != "exit":

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(message.encode('utf-8'))

            s.shutdown(socket.SHUT_WR)  # Signal the end of data

            data = s.recv(1024)
            print('Server:', repr(data.decode('utf-8')), '\n')

        message = input("Enter message to send: ").strip()
        print()
