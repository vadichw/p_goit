import math

RADIUS = 6371.01

lat1 = math.radians(50.45)
lon1 = math.radians(30.523)

lat2 = math.radians(51.5072)
lon2 = math.radians(-0.1275)

distance = math.acos((math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))) * RADIUS

print(distance)

# TERNALNI OPERATIONS

###
some_data = None
msg = some_data or "Nothing entered"
print(msg)

###
nice = False
state = "nice" if nice else "not nice"
print(state)

####



