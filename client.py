import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 5005

stop_receive_thread = threading.Event()

def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print('CONEXÃO ENCERRADA')
                break
            print(message)
            if stop_receive_thread.is_set():
                break
        except:
            break

def send_message(client_socket):
    while True:
        try:
            message = input()
            if (message.lower() == '/sair'):
                stop_receive_thread.set()
                client_socket.shutdown(socket.SHUT_RDWR)
                break
            client_socket.send(message.encode())
        except:
            break

def connect_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print('CONEXÃO COM O SERVIDOR ESTABELECIDA COM SUCESSO')

    receive_thread = threading.Thread(target=receive_message, args=(client_socket, ))
    receive_thread.start()

    send_message(client_socket)
    
    client_socket.close()
    sys.exit()

connect_server()