# from file_io import write_file, append_to_file, read_file

def write_file(file_name, file_content):
     file_name_str = str(file_name)
     with open(file_name_str + '.txt', 'w') as file:
        file.write(file_content)

def append_file(file_name, file_content):
     file_name_str = str(file_name)
     with open(file_name_str + '.txt', 'a') as file:
        file.write(file_content)

def read_file(file_name):
    file_name_str = str(file_name)
    with open(file_name_str + '.txt', 'r') as file:
        return file.read()