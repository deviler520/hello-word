# encoding utf8


import os


def communicate(dispatcher_host, dispatcher_port, command):
    if "status" == command:
        return "OK"
    else:
        pass
    return "OK"
