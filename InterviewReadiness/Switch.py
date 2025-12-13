print(f'\nCase Switch using Match-Case from Python 3.10')
case_number = int(input("\nEnter any single digit number less than 4: "))

match case_number:
    case 1:
        result = "One"
    case 2:
        result = "Two"
    case 3:
        result = "Three"
    case _:
        result = "Out of Range"

print(f'Numnber entered by user is {case_number}', result)

print(f'\nCase Switch using Dictionary Mapping')

def Ten():
    return "Ten"
def Eleven():
    return "Eleven"
def Twelve():
    return "Twelve"

dict = {
    10: Ten,
    11: Eleven,
    12: Twelve
}

value = 11
result = dict.get(value, lambda: "Unknown")()
print(result)
