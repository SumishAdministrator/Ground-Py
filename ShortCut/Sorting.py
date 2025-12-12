# Sort all 0's to teh extreme right of the array list


array_list = [1, 0, 6, 4, 3, 0, 5, 0, 0, 2]
array_list_new = []
indx = 0
for number in array_list:
    if number == 0:
        array_list_new.insert(0, number)
    else:
        array_list_new.insert(len(array_list_new), number)
    print(f"At index {indx}, the list contains", (number))
    print(array_list_new)
    indx=indx+1