import socket
import threading

HOST = '0.0.0.0'
PORT = 5005

clients = []

def send_message(message, source_socket):
    for client in clients:
        if (client != source_socket):
            try:
                client.send(message)
            except:
                clients.remove(client)
                 
def handle_client(socket):
    socket.send("DIGITE SEU NOME:".encode())
    nick = socket.recv(1024).decode()

    new_user = f"{nick} chegou no chat!"

    print(new_user)
    send_message(new_user.encode(), socket)

    while True:
        try:
            message = socket.recv(1024)
            if not message:
                break
            
            send_message(f"({nick}): {message.decode()}".encode(), socket)
        except:
            break

    clients.remove(socket)
    socket.close()
    send_message(f"{nick} DESCONECTOU".encode(), socket)
    print(f"Tchau {nick}! Foi bom te ver aqui!")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5) # escuta até 5

    print("SERVIDOR INICIADO COM SUCESSO")

    while True:
        client_socket, client_adress = server_socket.accept()
        print(f"Conexão recebida vindo de : {client_adress}")
        
        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server()