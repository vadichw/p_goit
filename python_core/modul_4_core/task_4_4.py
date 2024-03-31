def get_grade(key):
    grade = {"F": 1, "FX": 2, "E": 3, "D" : 4, "C": 4, "B": 5, "A": 5}
    return grade.get(key)

def get_description(key):
    grade_1 = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D":"Satisfactorily","C": "Good", "B":"Very good" , "A": "Perfectly"}
    return grade_1.get(key)

print(get_grade("A"))
print(get_description("A"))

