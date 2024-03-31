def normal_name(list_name):
    new_names = list(map(lambda name: name.title(), list_name))
    return new_names
    

big_names = normal_name
print(big_names(["dan", "jane", "steve", "mike"]))