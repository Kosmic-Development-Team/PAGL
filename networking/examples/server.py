from networking import connection


conns = []


def msgen(data):
    return bytearray([len(data[0])]) + bytearray(data[0] + data[1], 'ascii')


def msgde(data):
    nl = int(data[0])

    return data[1:nl + 1].decode('ascii'), data[nl + 1:].decode('ascii')


def msghd(data):
    print(data[0] + ': ' + data[1])
    for c in conns:
        c.sendmessage(0, data)


def onconnect(client):
    conn = connection.Connection(client)
    conns.append(conn)

    def oc():
        conns.remove(conn)
        print('Someone has left the chat')
    conn.onclose(oc)
    print('A new client has joined the chat!')
    conn.registerhandler(0, msghd)
    conn.open()

ip = input('Bind to: ')

connection.registertype(0, msgen, msgde)
server = connection.server(ip, onconnect)
server.start()
print('Server started')
