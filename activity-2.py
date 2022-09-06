n2 = 2
n3 = 3
n4 = 4
n5 = 5

for2 = 'First ten multiples of 2: '
print(for2, end = '')
for i in range(n2, (n2*10)+1):
    if (i % 2 == 0):
      print(i, end = " ")
print()
      
for3 = 'First ten multiples of 3: '
print(for3, end = '')
for i in range(n3, (n3*10)+1):
    if (i % 3 == 0):
      print(i, end = " ")
print()
      
for4 = 'First ten multiples of 4: '
print(for4, end = '')
for i in range(n4, (n4*10)+1):
    if (i % 4 == 0):
      print(i, end = " ")
print()
      
for5 = 'First ten multiples of 5: '
print(for5, end = '')
for i in range(n5, (n5*10)+1):
    if (i % 5 == 0):
      print(i, end = " ")