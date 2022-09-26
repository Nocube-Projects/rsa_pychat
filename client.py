# Importing modules
import socket
import threading

HOST = "127.0.0.1"
PORT = 1234

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
    except:
        print(f"Unable to connect to {HOST}:{PORT}")


if __name__ == "__main__":
    main()