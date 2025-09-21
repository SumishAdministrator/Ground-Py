with open("Sample.txt", "r") as file:
    content = file.read()
    print(content)

print ("+++++++++++++++++++++++")

with open("Sample.txt", "r") as file_t:
    line1 = file_t.readline()
    line2 = file_t.readline()
    print(line1)
    print(line2)

print ("___________________________________")

with open("Sample.txt", "r") as file_s:
    lines = file_s.readlines()
    print(lines)

print ("***********************************")



word_list = []

with open("Sample.txt", "r") as file_o:
        for words in file_o:
            word_list.extend(words.split())
        print(word_list)


