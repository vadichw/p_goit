def formatted_numbers():
    num_list = ["|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")]
    for num in range(16):
        num_list.append("|{:<10d}|{:^10x}|{:>10b}|".format(num, num, num))
    return num_list
for el in formatted_numbers():
    print(el)





#def formatted_numbers():
    #table = []

    # Header
    #header = "| {:<10} | {:^10} | {:>10} |".format("decimal", "hex", "binary")
    #table.append(header)
    
    #Separator
    #separator = "-" * len(header)
    #table.append(separator)

    # Data rows
    #for i in range(16):
        #decimal = "{0:<10d}".format(i)
        #hex = "{0:^10o}".format(i)
        #binary = "{0:>10b}".format(i)
        ###
        #line = "| {} | {} | {} |".format(decimal, hex, binary)
        #table.append(line)

    #return table

#for el in formatted_numbers():
    #print(el)

###
