def format_ingredients(items):
    if not items:
        return f"Nothing"
    if len(items) == 1:
        return items[0]
    # result = ', '.join(map(str, items[:-1]))
    result = f"{', '.join(items[:-1])} and {items[-1]}"
    # result += f' and {str(items[-1])}'
    return result

print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))

print(format_ingredients(["2 eggs"]))

print(format_ingredients([]))