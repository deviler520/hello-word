# encoding utf8


import os
import socket


def communicate(dispatcher_host, dispatcher_port, command):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((dispatcher_host, dispatcher_port))
    s.sendall(command)
    print(s.recv(1024))


if __name__ == "__main__":
    communicate("127.0.0.1", 8080, b"status")
