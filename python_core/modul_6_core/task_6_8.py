def save_applicant_data(source, output):
    
    with open(output, 'w',) as file:
        
        for element in source:
            line = f"{element['name']},
            {element['specialty']},
            {element['math']},
            {element['lang']},
            {element['eng']}\n"

            file.write(line)