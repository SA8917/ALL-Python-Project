import socket
import threading

choice = input("Do you want to host then enter 1 or if you want to connect then enter 2: ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.0.164", 9999))
    server.listen()

    client, _= server.accept()

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.0.164", 9999))

else:
    exit()


def sending_message(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("YOU:" + message)

def receive_messages(c):
    while True:
        print("Friend: " + c.recv(1024).decode())

threading.Thread(target=sending_message, args=(client,)).start()
threading.Thread(target=receive_messages, args=(client,)).start()