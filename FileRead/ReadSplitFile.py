def file_read_split(file_path):
    word_list = []
    try:
        with open(file_path, "r") as file_a:
            for words in file_a:
                word_list.extend(words.split())
            print(f"The new list is", word_list)
    except FileNotFoundError:
        print (f"The file path doesnt exists")

    return word_list
#file_path = '/Users/sumish/Documents/PythonProjects/Repo/Ground-Py/FileRea/Sample.txt'
file_path = 'Sample.txt'

calling_function = file_read_split(file_path)
print (calling_function)