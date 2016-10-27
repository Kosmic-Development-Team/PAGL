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
        self.oncloserun = []  # list of lambda-0
        self.handlers = {}  # byte to lambda-1

    def close(self):
        self.closed = True
        self.sock.close()
        self.handlers.clear()
        for l in self.oncloserun:
            l()
        self.oncloserun.clear()

    def onclose(self, lamb):
        self.oncloserun.append(lamb)

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
        return threading.Thread(target=lambda: receive(self))

    def registerhandler(self, byteid, handler):
        self.handlers[byteid] = handler

    def sendmessage(self, byteid, data):
        self.sock[0].sendall(bytearray(byteid) + encoder[byteid](data))


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


def sendmessage(byte, data, conn):
    message = encoder[byte](data)
    conn.sock[0].sendall(message)


def server(onconnect):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((mainaddr, mainport))
    sock.listen(1)

    def acceptclients():
        while True:
            client = Connection(sock.accept())
            time.sleep(5)
            onconnect(client)

    return threading.Thread(target=acceptclients)
