# \r
#print("vadimius", end= "\r")
#print(2001)



#start_ind = string.find("[")
#end_ind = string.find("]")
#new_string = string[:start_ind] + string[end_ind + 1:]

#string = "Виключити із цієї [групи] символи [розташовані між] дужками [, ]"

def sanitize(string):
    new_string = string[:]
    while True:
        start_ind = new_string.find("[")
        end_ind = new_string.find("]")
        if start_ind == -1:
            break
        new_string = new_string[:start_ind] + new_string[end_ind + 1:]
    return new_string
#print(sanitize("Виключити із цієї [групи] символи [розташовані між] дужками [, ]"))



### isdigit()
info = "Патрокл был одним из ближайших друзей и советников диадоха Селевка I Никатора[5][6]. Вместе с ним, по мнению Д. Грэйнджера, Патрокл бежал в 315 году до н. э. из Вавилонии[fr] в Египет, когда Селевку, в числе других сатрапов, грозила смерть в ходе репрессий Антигона. В 312 году до н. э. войско Антигона под командованием Деметрия Полиоркета было разбито при Газе"

# К-ство ЧИСЕЛ
def count_digit(info):
    count = 0
    for element in info:
        if element.isdigit():
            count += 1
    return count
#print(count_digit(info))

def count_num(info):
    count_num = 0
    position = 0
    nums = []
    while position < len(info):
        if info[position].isdigit(): # Нашли начало числа 
            num = ""
            while position < len(info) and info[position].isdigit(): # Ищем конец числа 
                num = num + info[position]
                position += 1
            nums.append(num)
            count_num += 1
        else:
            position = position + 1
    return count_num, nums # Если через запятую указать в ретерне, то вернет КОРТЕЖ

#print(count_num(info))

### isdigit()
numbers = ["1", "5", "10", "7", "2a", "abc"]

def sanitize(data):
    result = []
    for elem in data:
        if elem.isdigit():
            result.append(int(elem))
    return result
nums = sanitize(numbers)

#print(nums)
#print(sorted(nums))
#print(max(nums) - min(nums))
#print(sum(nums) / len(nums)) # 23 / 4 = 5.75


### join, split()
string = "I leant Python. I like it"
sl = string.split(". ")
text = ". ".join(sl)
#print(sl)
#print(text)

# Парсим query запит Гугл Method REPLACE
phone = "+ 1-234-567-89-10"
url_search = "https://www.google.com/search?q=%D0%BA%D0%BE%D1%82&newwindow=1&sca_esv=580461025&rlz=1C1SQJL_ruUA944UA944&sxsrf=AM9HkKkJWnLFP82TQi6dVImoYn8fzXj97w%3A1699446548304&ei=FH9LZeqhEpOowPAPwcS1gA4&ved=0ahUKEwjq-83es7SCAxUTFBAIHUFiDeAQ4dUDCBA&uact=5&oq=%D0%BA%D0%BE%D1%82&sclient=gws-wiz-serp"

edited_phone = phone.replace("-", " ")
edited_phone_1 = phone.replace("-", " ",2)
_, query = url_search.split("?")
#print(query)

obj_query = {}
for elem in query.split("&"):
    key, value = elem.split("=")
    obj_query.update({key: value.replace("+", " ")})
#print(obj_query)

#print(edited_phone)
#print(edited_phone_1)


## split(), removeprefix(), format()

phones = ["380681767600", "067451245301", "245485545415", "+38(050)1234555"]
codes_operator = {"067", "068", "097", "098,", "050"}

def is_valid_phone(phone: str) -> bool:
    def is_valid_operator(phone):
        if phone[:3] in codes_operator:
            return True
        return False
    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == "38":
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
def sanitaze_phone(phone):
    new_phone = (phone.strip()
                 .removeprefix("+")).replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    return new_phone


if __name__ == "__main__":
    for phone in phones:
        phone = sanitaze_phone(phone)
        is_valid = is_valid_phone(phone)
        if is_valid:
            print("Phone {:>12} is valid.".format(phone))
        else:
            print("Phone {:>12} is invalid.".format(phone))


        






