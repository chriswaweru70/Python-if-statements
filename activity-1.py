from ast import If
from xmlrpc.client import Boolean

print("Please enter the color of the flower (Blue/Red): ")
color = input() 

print("Please enter the size of the flower in inches: ")
sizeString = input()
size = float(sizeString)


if color == 'blue' and size < 2 and size > 0:
    print('Blue and small') 
elif color == 'blue' and size >= 2:
    print("Blue and large")
elif color == 'red' and size < 2 and size > 0:
    print("Red and small")
elif color =='red' and size >= 2:
    print("Red and large")
elif size <= 0 or '':
   print("Error: The size must be above 0")
elif color != 'red' or 'blue':
    print("invalid color value")
elif size >= '':
        print("You did not input a number")
else :
    input("invalid input")
