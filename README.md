# 💬 Chat TCP com Python (Cliente/Servidor)

Este projeto implementa um **sistema de chat em tempo real** usando **sockets TCP** e **threads** em Python.  
Permite a comunicação entre múltiplos clientes conectados ao mesmo servidor, com histórico das últimas mensagens.

---

## 🚀 Funcionalidades

- Comunicação em tempo real entre vários clientes.  
- Histórico das **últimas 10 mensagens** visível a novos usuários.  
- Identificação por **apelido (nickname)**.  
- Mensagens de **entrada e saída** de usuários no chat.  
- Encerramento limpo da conexão usando o comando `/sair`.  
- Controle de concorrência com `threading.Lock` para evitar condições de corrida no histórico.

---

## 🧩 Estrutura do Projeto

📂 chat_socket/  
├── server.py # Código do servidor  
└── client.py # Código do cliente  

---

## ⚙️ Como Executar

### 1️⃣ Inicie o Servidor

```python
python server.py
```
O servidor será iniciado escutando na porta 5005 em todas as interfaces (0.0.0.0).

### 2️⃣ Conecte os Clientes

Em outro terminal (ou outro computador na mesma rede), execute:
```python
python client.py
```

Por padrão, o cliente tenta se conectar em **127.0.0.1:5005**.
Se o servidor estiver em outra máquina, altere o IP na variável HOST dentro de client.py:

```python
HOST = 'IP_DO_SERVIDOR'
```
💡 Comandos

+ /sair → encerra a conexão com o servidor.
+ Qualquer outra mensagem → será enviada ao chat.

--- 

🧱 Lógica de Funcionamento
Servidor (server.py):
+ Aceita conexões de múltiplos clientes.
+ Armazena e envia o histórico das 10 últimas mensagens.
+ Gerencia threads para cada cliente conectado.
+ Notifica os demais usuários sobre entradas e saídas.

👨🏻‍💼 Cliente (client.py):
+ Conecta ao servidor.
+ Envia e recebe mensagens em threads separadas.
+ Permite encerrar a conexão de forma limpa com /sair.

---

⚠️ Observações

O cliente e o servidor devem estar na mesma rede local (ou usar redirecionamento de portas).

Certifique-se de que a porta 5005 **não está sendo bloqueada pelo firewall**.

Este projeto **não utiliza WebSockets** — é baseado em TCP puro com sockets.
