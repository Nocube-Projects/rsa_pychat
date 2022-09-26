# Importing Modules
import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

connections = []

def listening(client, username):
    
    while True:
        message = client.recv(2048).decode("utf-8")#

        if message != "":
            final_msg = username + "~" + message
            broadcast(final_msg)

        else:
            print(f"Message recieved from {username} is empty")
        
def direct_message(client, message):

    client.sendall(message.encode("utf-8"))

def broadcast(message):
    
    for user in connections:
        direct_message(user[1], message)

def handle_client(client):
    
    while True:
        username = client.recv(2048).decode("utf-8")
        
        # New user
        if username != "":
            connections.append((username, client))
            break

        else:
            client.send("Username empty".encode("utf-8"))

    thread = threading.Thread(target=listening, args=(client, username))
    thread.start()

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server.bind((HOST, PORT))
        print(f"Running on {HOST}:{PORT}")

    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

    server.listen()

    while True:
        client, address = server.accept()
        print(f"Connected to {address}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
        print(f"Active connections {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()