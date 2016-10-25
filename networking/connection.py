import socket
import threading
import time

mainport = 24680
mainaddr = 'localhost'


class Connection:
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.types = {}  # byte to runnable (lambda)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, addr):
        Connection(addr, mainport)


def server(self, onconnect):
    def acceptclients():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((mainaddr, mainport))
        sock.listen(1)
        while True:
            client = sock.accept()
            time.sleep(5)
            onconnect(client)

    return threading.Thread(target=acceptclients())
