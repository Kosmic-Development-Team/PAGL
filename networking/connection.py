import socket
import threading
import time

mainport = 24680
mainaddr = 'localhost'

encoder = {}  # byteid to lambda-1 ret bytes
decoder = {}  # byteid to lambda-1 ret data


class Connection:
    def __init__(self, sock):
        self.sock = sock
        self.closed = False
        self.onclose = []  # list of lambda-0
        self.handlers = {}

    def close(self):
        self.closed = True
        self.sock.close()
        self.handlers.clear()
        all(l() for l in self.onclose)
        self.onclose.clear()

    def onclose(self, lamb):
        self.onclose.append(lamb)

    def processmessage(self, byteid, bytedata):
        if not isinstance(self.handlers[byteid], None):
            self.handlers.get(byteid)(decode(byteid, bytedata))
        else:
            print("Unknown message id:", byteid)
            self.close()

    def open(self):
        def receive(conn):
            while not conn.closed:
                try:
                    bid = conn.sock.recv(256)
                    info = bytearray()
                    while bid:
                        info.append(bytearray(bid))
                        bid = conn.sock.recv(256)
                    conn.processmessage(info[0], info[1:])
                except:
                    pass
        threading.Thread(target=receive(self)).run()

    def registerhandler(self, byteid, handler):
        self.handlers[byteid] = handler

    def sendmessage(self, byteid, data):
        self.sock.sendall(bytearray(byteid).append(encoder[byteid](data)))


def decode(byteid, bytedata):
    return decoder[byteid](bytedata)


def encode(byteid, data):
    return encoder[byteid](data)


def connect(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, mainport))
    return Connection(sock)


def registertype(byte, en, de):  # look above
    encoder[byte] = en
    decoder[byte] = de


def sendmessage(byte, data):
    message = encoder[byte](data)


def server(onconnect):
    def acceptclients():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((mainaddr, mainport))
        sock.listen(1)
        while True:
            client = sock.accept()
            time.sleep(5)
            onconnect(client)

    return threading.Thread(target=acceptclients())
