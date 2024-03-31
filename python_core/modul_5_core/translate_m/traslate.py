trans_map = {ord("В"):"V",
             ord("а"): "a",
             ord("д"): "d",
             ord("и"): "i",
             ord("м"): "m",
             ord("о"): "o"}
#ukr_name = "Вадим"
#lat_name = ukr_name.translate(trans_map)
#print(ukr_name, lat_name)

text = "Hellо, wоrld"
indx = text.find("world") # O на укр.
new_indx = text.translate(trans_map).find("world")
print(indx)
print(new_indx)