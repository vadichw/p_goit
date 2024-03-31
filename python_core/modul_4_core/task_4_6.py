def split_list(grade):
    if not grade:
        return [],[]
        
    average = sum(grade) / len(grade)

    list_1 = [x for x in grade if x <= average]
    list_2 = [x for x in grade if x > average]

    return list_1, list_2
print(split_list([10,5,1,7,5,6]))  