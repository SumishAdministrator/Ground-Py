#This is to show how "except" code block can handle the known/unknow errors if generated while during teh execution of "try" block

try:
    numerator = float(input("\n Enter a number as numerator: \n "))
    denominator = float(input("Enter a number as denomintaor: \n "))
    quotient = float(numerator / denominator)
    print(f"The quotient is:", quotient)
    print(f"The quotient retrieved is, {quotient}.")
except ValueError:
    print("We have an error in the user input. Please enter a valid Number > 0")

except ZeroDivisionError:
    print("We have an error in the user input. Please enter a Non-Zero Denominator")