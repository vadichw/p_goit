# Реалізуйте функцію encode_data_to_base64(data), яка приймає у параметрі data зазначений список, виконує кодування кожної пари username:password у формат Base64 та повертає список із закодованими парами username:password у вигляді:
# ['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

import base64

def encode_data_to_base64(data):
    list = []

    for pair in data:
        username, password = pair.split(':')
        string = f"{username}:{password}".encode()
        encoded_string = base64.b64encode(string).decode('utf-8')

        list.append(encoded_string)
    return list