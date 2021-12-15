# client.py
import socket
import threading
import cezar

nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"  # "127.0.1.1"
port = 8002
my_socket.connect((host, port))


def thread_sending():
    while True:
        message_to_send = input()
        if message_to_send:
            message_with_nickname = nickname + " : " + message_to_send
            cezar.myencode(message_with_nickname)                       #шифруєм повідомлення що надсилаємо
            my_socket.send(message_with_nickname.encode())


def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        cezar.mydecode(message)                     #дишифруєм повідомлення що отримуєм
        print(message)


thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()