from networking import connection
import threading


def msgen(data):
    return bytearray([len(data[0])]) + bytearray(data[0] + data[1], 'ascii')


def msgde(data):
    nl = int(data[0])
    return data[1:nl + 1].decode('ascii'), data[nl + 1:].decode('ascii')


name = input('Username: ')
ip = input('Connect to: ')


def msghd(data):
    if not data[0] == name:
        print('\r' + data[0] + ': ' + data[1])

connection.registertype(0, msgen, msgde)
client = connection.connect(ip)
client.registerhandler(0, msghd)
client.open()


def chat():
    while not client.closed:
        msg = input('')
        if msg == '/exit':
            client.close()
        else:
            client.sendmessage(0, (name, msg))
threading.Thread(target=chat).start()

#client = connection.connect('localhost')
#mssg = ''
#while not mssg == 'exit':  # bytearray([len(mssg)]) +
#    mssg = input("~")
#    print(bytearray([len(mssg)]))
#    client.sock.send(bytearray([len(mssg)]) + bytearray(mssg, 'ascii'))
#client.sock.close()
