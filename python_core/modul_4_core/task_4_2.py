def prepare_data(data):
    new_list = data
    new_list.sort()
    new_list.pop(0)
    new_list.pop(-1)
    return new_list

print(prepare_data([1,2,3,50,-10]))