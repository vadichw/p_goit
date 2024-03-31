from pprint import pprint

def get_recipe(path, search_id):
    with open(path, 'r') as file:
        for line in file:
            recept_data = line.strip().split(',')
            id, name, *ingredients = recept_data

            if id == search_id:
                return {
                    'id' : id,
                    'name' : name,
                    'ingredients' : ingredients,
                }
    return None

pprint(get_recipe('test.txt', '60bc4613067a15887e1ae5'))