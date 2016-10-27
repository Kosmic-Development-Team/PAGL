from networking import connection


ciid = 0
clients = []
servname = 'Cruz\'s Fun Chat'


class ClientInfo:
    def __init__(self, conn):
        self.conn = conn
        self.name = 'NewClient'


def onconnect(c):
    nc = ClientInfo(c)
    clients.append(nc)
    print('New Client has joined the Chat')

    def oc(cn):
        clients.remove(cn.conn)
        print(cn.name + ' has left the Chat')
    nc.conn.onclose(lambda: oc(nc))

    def rcn(cn, name):
        print(cn.name + ' has been id\'d as ' + name)
        cn.name = name
    nc.conn.registerhandler(0b00000001, lambda d: rcn(nc, d))
    nc.conn.sendmessage(0b00000001, servname)
    nc.conn.open()


print('Server begin')
connection.mainport = 25565
server = connection.server(lambda c: onconnect(c))
print('Server init')


def cme(nm):
    bts = bytearray()
    name = nm[0]
    bts.append(len(name))
    bts.extend(map(ord, name))
    bts.extend(map(ord, nm[1]))
    return bts


def cmd(data):
    ns = data[0]
    nm = data[1:].decode('ascii')
    return nm[0:ns], nm[ns:]


connection.registertype(0b00000000, lambda d: cme(d), lambda d: cmd(d))
connection.registertype(0b00000001, lambda n: bytearray(n, 'ascii'), lambda d: d.decode('ascii'))

print('Starting the server')
server.start()
