import socket
import threading

HOST = '0.0.0.0'
PORT = 5005

clients = []
message_history = [] #pra armazenar o historico das 10 msg
history_lock = threading.Lock() #pra garantir que o historico não vai ser modificado por duas threads at the same time

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

    try: #aqui vai enviar o historico pra o novo client
        socket.end("\n--- Histórico das últimas 10 mensagens ---".encode())
        with history_lock:
            for msg in message_history:
                socket.send(msg.encode())
        socket.send("--------------------------------------------------\n".encode())
    except:
        pass #ignora o betinha se desconectar aqui
    
    send_message(new_user.encode(), socket)

    while True:
        try:
            message = socket.recv(1024)
            if not message:
                break

            formatted_message = f"({nick}): {message.decode()}" #na hora do send_message

            with histoy_lock: #adiciona msg nova ao historico
                message_history.append(formatted_message)
                if len(message_history) > 10: #aqui garante o max de 10 msg
                    message_history.pop(0) #remove a mais antiga
            
            send_message(formatted_message.encode(), socket) #papo de clean code foi mal
        except:
            break

    clients.remove(socket)
    socket.close()

    disconnect_msg = f"{nick} DESCONECTOU"

    with history_lock: #aqui tbm pra adicionar a mensagem de desconnect no historico
        message_history.append(disconnect_msg)
        if len(message_history) > 10:
            message_history.pop(0)
    
    send_message(disconnect_msg.encode(), socket)
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
