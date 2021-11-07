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
count = 0
numbers = None


def warmup_first(response_data: str):
    global state
    str_numbers = response_data.split(' ')
    if len(str_numbers) is not 3:
        raise Exception("Количество числе: " + str(len(str_numbers)))
    state = None
    return "".join([str(int(str_numbers[i]) ** 2) + " " if i is not 2 else str(int(str_numbers[i]) ** 2) for i in range(len(str_numbers))])


def warmup_second(response_data: str):
    global first_string, state
    if first_string is None:
        first_string = response_data
        return None
    concat = first_string + response_data
    state = first_string = None
    return concat


def warmup_third(response_data: str):
    global command, state
    print(command, " ", state, " ", response_data)
    if command is None:
        command = int(response_data)
        return None
    if command is 0:
        state = command = None
        return str(int(response_data) ** 2)
    if command is 1:
        command = int(response_data)
        return None
    state = command = None
    return None


def task_first(response_data: str):
    global state, count
    if int(response_data) is 0:
        tmp_count = count
        state, count = None, 0
        return str(tmp_count)
    count = count + 1
    return None


def task_second(response_data: str):
    global state, numbers
    if numbers is None:
        numbers = response_data.split(' ')
        return None
    strings = response_data.split(' ')
    result_str = "".join(["'" + n + " " + s + "'" for s in strings for n in numbers])
    state = numbers = None
    return result_str


def choose_job(response_data: bytes):
    global state, command, first_string, count, numbers
    try:
        if state is None:
            state = int(data.decode())
            return None
        if state is 1:
            return warmup_first(response_data.decode())
        if state is 2:
            return warmup_second(response_data.decode())
        if state is 3:
            return warmup_third(response_data.decode())
        if state is 4:
            return task_first(response_data.decode())
        if state is 5:
            return task_second(response_data.decode())
        state = None
    except Exception as ex:
        print(ex)
        state = command = first_string = numbers = None
        count = 0
        return None


while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    try:
        print('Подключено к:', client_address)
        while True:
            data = connection.recv(100)
            # has_data = True if len(data) > 1 else False
            # while has_data:
            #     resp_data = connection.recv(100)
            #     has_data = True if resp_data else False
            #     data = data + resp_data
            if data:
                result = choose_job(data)
                if result:
                    connection.sendall(result.encode())
                else:
                    connection.sendall("None".encode())
    finally:
        connection.close()
