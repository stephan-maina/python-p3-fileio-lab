def write_file(file_name, file_content):
    try:
        with open(f"{file_name}.txt", mode="w") as file_open:
            file_open.write(file_content)
        print(f'Successfully wrote to "{file_name}.txt".')
    except Exception as e:
        print(f'Error writing to file: {e}')

def append_file(file_name, append_content):
    try:
        with open(f"{file_name}.txt", mode="a") as file_append:
            file_append.write(append_content)
        print(f'Successfully appended to "{file_name}.txt".')
    except Exception as e:
        print(f'Error appending to file: {e}')

def read_file(file_name):
    try:
        with open(f"{file_name}.txt", mode="r") as open_file:
            return open_file.read()
    except FileNotFoundError:
        print(f'File not found: "{file_name}.txt"')
    except Exception as e:
        print(f'Error reading file: {e}')

# Example usage:
# write_file("example", "Hello, World!")
# append_file("example", "\nAppended Text.")
# content = read_file("example")
# print(content)
