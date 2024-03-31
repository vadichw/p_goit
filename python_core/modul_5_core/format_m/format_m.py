#number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#header = "|{:^15}|{:^15}|{:^15}|".format("int", "int^2,", "int^3")
#separator = "-" * len(header)
#body = ""
#for num in number:
    #body += "|{:^15}|{:^15}|{:^15}|\n".format(num, num**2, num**3)
#table = "\n".join([separator, header, separator,body,separator])
#print(table)
#print(separator, header, separator, sep = '\n')


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
header = "|{:^15}|{:^15}|{:^15}|{:^15}|".format("int", "dex", "oct", "bin")
separator = "-" * len(header)
body = ""
for num in number:
    body += "|{0:^15d}|{0:^15x}|{0:^15o}|{0:^15b}\n".format(num, )
table = "\n".join([separator, header, separator,body,separator])
print(table)
