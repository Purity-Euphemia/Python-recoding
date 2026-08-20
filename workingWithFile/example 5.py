try:
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip()) # Using strip to remove the newline character
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")