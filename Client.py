import socket

sock = socket.socket()
sock.connect(('localhost', 10004))
while True:
    value = input()
    sock.send(bytes(value, encoding='utf-8'))
    data = sock.recv(100).decode()

    if data != "None":
        print(data)

# sock.close()

# print(data)