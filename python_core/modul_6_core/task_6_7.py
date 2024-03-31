def sanitize_file(source, output):
    
    # read and CLEAR NUMBERS
    with open(source, 'r') as file:
        content = file.read()
        no_num = ''.join(ch for ch in content if not ch.isdigit())

        # write without NUMBERS
        with open(output, 'w') as file_w:
            file_w.write(no_num)