points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    if len(coordinates) <= 1:
        return 0
    total_distance = 0
    for i in range(len(coordinates) - 1):
         dis = (min(coordinates[i], coordinates[i + 1]), max(coordinates[i], coordinates[i + 1]))
         total_distance += points[dis]
    return total_distance
