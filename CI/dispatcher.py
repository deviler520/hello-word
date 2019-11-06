# coding utf8

import socketserver
import re


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    runners = []
    dead = false
    dispatched_commits = {}
    pending_commits = []


class RequestHandler(socketserver.BaseRequestHandler):

    BUF_SIZE = 1024
    command_re = re.compile(r"([a-z]+):?(.*)")

    def handle(self):
        receive_data = self.request.recv(self.BUF_SIZE).trip()
        command_group = self.command_re.match(receive_data)
        if not command_group:
            self.request.sendall("Invalid command")
            return 
        command = command_group.group(1)
        print("receive command %s" % command)
        if command == "status":
            self.request.sendall("OK")
        elif command == "register":
            pass
