from ast import If, Return
from xmlrpc.client import Boolean


print("Welcome to the flower shop")

color = input("Enter the flower color you want: ") 
size = float(input("Enter the size you want:"))

if color == 'blue' and size<2:
    while (isinstance(size, float)) or size <=0:
        print("The size can't be negative, please restart:")
        print("Start again")   
    print('The flower is small Blue') 
elif color == 'blue' and size>=2:
    print("the flower is blue large")
elif color == 'red' and size<2:
    while (isinstance(size, float)) or size <=0:
        ("The size can't be negative, please restart:")
        print("Start again") 
    print("red small")
elif color =='red' and size>=2:
    print("red large")
elif color != 'red' or 'blue':
    print("Invalid Color")
else:
    print("invalid input")
