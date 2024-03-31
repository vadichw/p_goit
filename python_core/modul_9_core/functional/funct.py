import math

def length(d):
    result = d * math.pi
    return result

get_lambda = lambda d: d * math.pi
    

def get_ost(data):
    result = []
    for n in data:
        ost = n % 2
        result.append(ost)
    return result

def check_num(data):
    result = []
    for n in data:
        ost = n % 2
        if ost:
            result.append(n)
    return result


if __name__ == "__main__":
    # length_1 = length(10)
    # length_2 = get_lambda(10)
    # print(length_1, length_2, sep='\n')
    
    data = [1, 2, 3, 4, 5, 6,]
    # ost_1 = get_ost(data)
    # print(*ost_1)
    
    # ost_2 = map(lambda n: n % 2, data)
    # print(*ost_2)
    
    # check_data = check_num(data)
    # print(check_data)
    
    check_data_filter = filter(lambda x : x % 2, data)
    print(list(check_data_filter))