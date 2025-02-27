import sys

def is_num(input):

    if(len(input) == 0):
        return False
    for i in input:
        if((i != '-') and (not i.isdigit())):
            return False
    return True


if(len(sys.argv) > 2):
    print("AssertionError: more than one argument is provided")
    sys.exit()
elif(len(sys.argv) == 1):
    sys.exit()

a = sys.argv[1]
if not is_num(a):
    print("AssertionError: argument is not an integer")
    sys.exit()
#check if number is even or odd or 0
a = int(a)
if(a == 0):
    print("I'm Zero.")
elif(a % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
