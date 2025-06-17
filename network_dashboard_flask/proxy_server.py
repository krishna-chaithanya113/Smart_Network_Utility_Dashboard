import socket
import threading

def handle_client(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_data = remote_socket.recv(4096)
        client_socket.send(remote_data)

    while True:
        local_data = client_socket.recv(4096)
        if len(local_data) == 0:
            break
        remote_socket.send(local_data)

        remote_data = remote_socket.recv(4096)
        if len(remote_data) == 0:
            break
        client_socket.send(remote_data)

    client_socket.close()
    remote_socket.close()

def proxy_server(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((local_host, local_port))
    server.listen(5)

    print(f'[*] Listening on {local_host}:{local_port}')

    while True:
        client_socket, addr = server.accept()
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')

        proxy_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()
