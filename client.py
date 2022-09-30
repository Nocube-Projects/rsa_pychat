# Importing modules
import socket
import threading

import tkinter as tk
from tkinter import ttk
import sv_ttk

class menu:
    def __init__(self, master):
        
        # server details
        self.HOST = "185.215.180.30"
        self.PORT = 1234

        # ttk theme
        sv_ttk.set_theme("dark")

        # menu gui
        self.master = master
        self.master.title("Python Chat App")
        self.master.geometry("500x500")
        self.master.config(bg="Black")
        self.master.resizable(True, True)

    # Home menu GUI
    def home_menu(self):
        
        self.frame = ttk.Frame(self.master)
        #self.home_menu.place(x=0, y=0, width=500, height=500)

        # grid setup
        self.frame.columnconfigure(0, weight=1)

        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)

        # login button
        login_button = ttk.Button(self.frame, text="Login", command=self.main)
        login_button.grid(column=0, row=0, padx=0, pady=0)

        # register button
        register_button = ttk.Button(self.frame, text="Register")
        register_button.grid(column=0, row=1, padx=0, pady=0)

        #self.frame.place(x=0,y=0)
        self.frame.pack(fill="both", expand=1)

    # Listens for messages from the server
    def listening(self):
        
        while True:
            message = self.client.recv(2048).decode("utf-8")

            if message != "":
                username = message.split("~")[0]
                contents = message.split("~")[1]

                print(f"{username}: {contents}")
            else:
                print("Message is empty")

    def sending(self):
        
        while True:
            print("Type your message: ")
            message = input("")

            if message != "":
                self.client.sendall(message.encode("utf-8"))

            else:
                print("Message empty")

    def chat_to_server(self):
        
        username = input("Username: ")
        if username != "":
            self.client.sendall(username.encode("utf-8"))

        else:
            print("Username empty")
            self.chat_to_server()

        thread = threading.Thread(target=self.listening)
        thread.start()

        self.sending()

    def main(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.client.connect((self.HOST, self.PORT))
            print(f"Connected to {self.HOST}:{self.PORT}")
            

        except:
            print(f"Unable to connect to {self.HOST}:{self.PORT}")
            exit()

        self.chat_to_server()


if __name__ == "__main__":
    root = tk.Tk()
    R = menu(root)
    R.home_menu()
    root.mainloop()