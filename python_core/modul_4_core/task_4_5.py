def lookup_key(data, value):
    data = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}
    keys = []
    for key, val in data.items():
        if val == value:
            keys.append(key)
    return keys
print(lookup_key(None, 3))

