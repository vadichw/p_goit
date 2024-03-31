# [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for elem in employee_list:
        for people in elem:
            fh.write(people + '\n')
            
    fh.close()
    
print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']], 'test.txt'))