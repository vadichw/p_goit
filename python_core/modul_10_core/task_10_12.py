class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException("Employee ID must start with '01'")
    else:
        id_list.append(employee_id)
    return id_list