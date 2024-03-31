import socket


def main():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()

    connection, address = server_socket.accept()
    print(f'Connect from {address}')

    while True:
        msg = connection.recv(100).decode()
        if not msg:
            break
        print(f'Received message {msg}')

        message = input('-->')
        connection.send(message.encode())

    connection.close()


if __name__ == '__main__':
    main()
