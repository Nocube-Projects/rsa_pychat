# Importing Modules
import socket
import threading

HOST = "127.0.0.1"
PORT = 1234
LISTENER_LIMIT = 5

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server.bind((HOST, PORT))
        print(f"Running on {HOST}:{PORT}")
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        print(f"Connected to {address}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
        print(f"Active connections {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()