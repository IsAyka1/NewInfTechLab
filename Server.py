import socket
import sys

# сначала выключать клиента
# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 10004)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)

state = None
command = None
first_string = None
numbers = None


def warmup_first(response_data: str):
    global state
    str_numbers = response_data.split(' ')
    if len(str_numbers) != 3:
        raise Exception("Количество числел: " + str(len(str_numbers)))
    state = None
    return "".join([str(int(str_numbers[i]) ** 2) + " " if i != 2 else str(int(str_numbers[i]) ** 2) for i in range(len(str_numbers))])


def warmup_second(response_data: str):
    global first_string, state
    if first_string == None:
        first_string = response_data
        return None
    concat = first_string + response_data
    state = first_string = None
    return concat


def warmup_third(response_data: str):
    global command, state
    if command == None:
        command = int(response_data)
        return None
    if command == 0:
        state = command = None
        return str(int(response_data) ** 2)
    if command == 1:
        command = int(response_data)
        return None
    state = command = None
    return None


def task_first(response_data: str):
    global state
    state = None
    str_numbers = response_data.split(' ')
    if len(str_numbers) != 2:
        raise Exception("Количество числел: " + str(len(str_numbers)))
    str_multi = "Произведение: " + str(int(str_numbers[0]) * int(str_numbers[1]))
    str_sum = "Сумма: " + str(int(str_numbers[0]) + int(str_numbers[1]))
    return str_multi + " " + str_sum


def task_second(response_data: str):
    global state, command
    if command == None:
        if int(response_data) == 0:
            command = 0
            return None
        if int(response_data) != 0:
            command = 1
            return None
    if command == 0:
        state = command = None
        strings = response_data.split(' ')
        return "".join([s for s in strings])
    if command == 1:
        state = command = None
        str_numbers = response_data.split(' ')
        return str(sum([int(s) for s in str_numbers]))
    state = command = None
    return None

def choose_job(response_data: bytes):
    global state, command, first_string, numbers
    try:
        if state == None:
            state = int(response_data.decode())
            return None
        if state == 1:
            return warmup_first(response_data.decode())
        if state == 2:
            return warmup_second(response_data.decode())
        if state == 3:
            return warmup_third(response_data.decode())
        if state == 4:
            return task_first(response_data.decode())
        if state == 5:
            return task_second(response_data.decode())
        state = None
    except Exception as ex:
        print(ex)
        state = command = first_string = numbers = None
        return None


while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключено к:', client_address)
        while True:
            data = connection.recv(100)
            if data:
                result = choose_job(data)
                if result:
                    connection.sendall(result.encode())
                else:
                    connection.sendall("None".encode())
    finally:
        connection.close()
