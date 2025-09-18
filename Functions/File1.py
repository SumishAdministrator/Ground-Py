# Learn the application of __main__
#This is file1.py

def add (a, b):
    return a + b

if __name__ == '__main__':
    print ("True")
    if add(2, 2) == 4:
        print ("Pass")
    else:
        print ("Fail")

print(f"Print from File1 is called from {__name__}:",{add(2, 3)})