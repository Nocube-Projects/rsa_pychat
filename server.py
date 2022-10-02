# Importing Modules
import socket
import threading
from dotenv import load_dotenv
from os import getenv

#fix code

# Server processing class
class process:
    def __init__(self):
        
        load_dotenv()

        # Server details
        self.HOST = "0.0.0.0"
        self.PORT = 1234
        
        # DB details
        self.DB_HOST = "localhost"
        self.DB = "rsa_pychat"
        self.DB_USER = "rsa_pychat"
        self.DB_PASS = getenv("DBPASS")

        self.connections = []


    def listening(self):
        
        while True:
            message = self.client.recv(2048).decode("utf-8")

            if message != "":
                self.message = self.username + "~" + message
                self.broadcast()

            else:
                print(f"Message recieved from {self.username} is empty")
            
    def direct_message(self):

        self.client.sendall(self.message.encode("utf-8"))

    def broadcast(self):
        
        for user in self.connections:
            self.client = user[1]
            self.direct_message()

    def handle_client(self):
        
        while True:
            self.username = self.client.recv(2048).decode("utf-8")
            
            # New user
            if self.username != "":
                self.connections.append((self.username, self.client))
                self.message = "SERVER~" + f"{self.username} has joined the chat"
                self.broadcast()
                break

            else:
                self.client.send("Username empty".encode("utf-8"))

        thread = threading.Thread(target=self.listening)
        thread.start()

    def main(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            server.bind((self.HOST, self.PORT))
            print(f"Running on {self.HOST}:{self.PORT}")

        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

        server.listen()

        while True:
            self.client, address = server.accept()
            print(f"Connected to {address}")
            thread = threading.Thread(target=self.handle_client)
            thread.start()
            print(f"Active connections {threading.activeCount() - 1}")

if __name__ == "__main__":
    m = process()
    m.main()
