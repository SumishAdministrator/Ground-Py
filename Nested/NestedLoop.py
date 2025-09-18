#This code is to determine the nested loops

list_number = ['1', '2', '3', '4']
list_chars = ['A', 'B', 'C']

for numbers in list_number:
    for letters in list_chars:
        print(f"{numbers}{letters}", end = " ")
    print ()
