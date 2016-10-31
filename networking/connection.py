import socket
import threading


port = 25565
packsize = 16
acceptclients = True
decoders = {}  # byte to lambda-1 ret
encoders = {}  # byte to lambda-1 ret


class Connection:
    def __init__(self, sock):
        self.sock = sock
        self.closed = False
        self.closing = []
        self.handlers = {}  # byte to lambda-1

    def onclose(self, lamb):
        self.closing.append(lamb)

    def close(self):
        self.closed = True
        self.sock.close()
        self.handlers.clear()
        for l in self.closing:
            l()
        self.closing.clear()

    def process(self, data):
        byteid = data[0]
        if byteid in self.handlers:
            self.handlers[byteid](decoders[byteid](data[1:]))

    def open(self):
        def receive(client):
            try:
                buffer = bytearray()
                while True:
                    if len(buffer) > 0:
                        dl = buffer[0]
                        buffer = buffer[1:]
                        while len(buffer) < dl:
                            buffer += client.sock.recv(packsize)
                        client.process(buffer[0:dl])
                        buffer = buffer[dl:]
                    else:
                        buffer += client.sock.recv(packsize)
            except ConnectionResetError:
                client.close()
        threading.Thread(target=lambda: receive(self)).start()

    def registerhandler(self, byteid, handler):
        self.handlers[byteid] = handler

    def sendmessage(self, byteid, data):
        msg = bytearray([byteid]) + encoders[byteid](data)
        msg = bytearray([len(msg)]) + msg
        self.sock.sendall(msg)


def registertype(byteid, en, de):
    encoders[byteid] = en
    decoders[byteid] = de


def connect(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    return Connection(sock)


def server(ip, onconnect):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)

    def acceptconn():
        while True:
            if acceptclients:
                client = sock.accept()[0]
                onconnect(client)
    return threading.Thread(target=acceptconn)
