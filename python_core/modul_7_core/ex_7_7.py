def data_preparation(list_data):
    cleaned_data = []

    for sublist in list_data:
        if len(sublist) > 2:
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))
        cleaned_data.extend(sublist)

    return sorted(cleaned_data, reverse=True)


list_of_lists = [[1, 2, 3], [3, 4], [5, 6]]
result = data_preparation(list_of_lists)
print(result)
