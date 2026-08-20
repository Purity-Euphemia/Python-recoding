try:
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())