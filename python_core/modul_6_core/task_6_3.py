def read_employees_from_file(path):
    fh = open(path, 'r')
    lines = fh.readlines()
    lines = [line.strip() for line in lines] # Удалить \n
    fh.close()
    return lines