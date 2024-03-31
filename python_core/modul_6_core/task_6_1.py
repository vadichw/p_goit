# Alex Korp,3000
#Nikita Borisenko,2000
#Sitarama Raju,1000

def total_salary(path):
    salary = 0.0
    file = open(path, 'r')
    line = file.readline()
    while line:
        name, salary_num = line.strip().split(',')
        salary += float(salary_num)
        line = file.readline()
    file.close()
    return salary


