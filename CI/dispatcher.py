# coding utf8

import socketserver
import re

from pip import __main__


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    runners = []
    dead = False
    dispatched_commits = {}
    pending_commits = []


class RequestHandler(socketserver.BaseRequestHandler):
    BUF_SIZE = 1024
    command_re = re.compile(r"([a-z]+):?(.*)")

    def handle(self):
        receive_data = self.request.recv(self.BUF_SIZE).decode().strip()
        print("receive_data %s" % receive_data)
        command_group = self.command_re.match(receive_data)
        if not command_group:
            self.request.sendall("Invalid command")
            return
        command = command_group.group(1)
        print("receive command %s" % command)
        if command == "status":
            self.request.sendall(b"status OK")
        elif command == "register":  # "register:127.0.0.1:8080"
            host, port = command_group(2).split(":")
            self.server.runners.append({"host": host, "port": port})
            self.request.sendall(b"register OK")


def server(host, port):
    dispatch_server = ThreadingTCPServer((host, port), RequestHandler)
    dispatch_server.serve_forever()


if __name__ == "__main__":
    server("127.0.0.1", 8080)
