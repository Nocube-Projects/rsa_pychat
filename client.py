# Importing modules
import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

# Listens for messages from the server
def listening(client):
    
    while True:
        message = client.recv(2048).decode("utf-8")

        if message != "":
            username = message.split("~")[0]
            contents = message.split("~")[1]

            print(f"{username}: {contents}")
        else:
            print("Message is empty")

def sending(client):
    
    while True:
        print("Type your message: ")
        message = input("")

        if message != "":
            client.sendall(message.encode("utf-8"))

        else:
            print("Message empty")

def chat_to_server(client):
    
    username = input("Username: ")
    if username != "":
        client.sendall(username.encode("utf-8"))

    else:
        print("Username empty")
        chat_to_server(client)

    thread = threading.Thread(target=listening, args=(client,))
    thread.start()

    sending(client)

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

    except:
        print(f"Unable to connect to {HOST}:{PORT}")

    chat_to_server(client)

if __name__ == "__main__":
    main()