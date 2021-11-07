import socket

sock = socket.socket()
sock.connect(('localhost', 10004))
while True:
    value = input()
    sock.send(bytes(value, encoding='utf-8'))
    data = sock.recv(100).decode()
    # print(data)
    # has_data = True if data != "None" else False
    # print(has_data)
    # while has_data:
    #     resp_data = sock.recv(100).decode()
    #     has_data = True if resp_data else False
    #     data = data + resp_data
    if data != "None":
        print(data)

# sock.close()

# print(data)