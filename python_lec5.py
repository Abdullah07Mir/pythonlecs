#  WAP to print the numbers from 1 to 100 using while loop.

num = 1
while num<=100:
    print(num)
    num+=1

print("end of the program")

num = 100
while num>=1:
    print(num)
    num-=1

print("end of the program")

# WAP to print the multiplication table of a number using while loop.

val = int(input("Enter a number you want the multiplication table for:"))
i=1
while i<=10:
    z=val*i
    print(z)
    i+=1
print("end of the program")

# WAP to print the elements of a list using while loop.

x =[1,4,9,16,25,36,49,64,81,100]
i=0
while i<= len(x)-1:
    print("the list element no. i is:", x[i])
    i+=1
print("end of the program")

# WAP to search a value in a tuple using while loop and if else statement.  
tup = (1,4,9,16,25,36,49,64,81,100)

ser= int(input("Enter value to search:"))

i=0

while i< len(tup):
    if(tup[i]==ser):
        print("value found at index:", i)
        break
    i+=1
else:
    print("value not found in the tuple")

print("end of the program ")

# WAP to print the elements of a list using for loop.

el_list =[1,4,9,16,25,36,49,64,81,100]

print("ELements of the list are:")
for i in el_list:
    print(i)

# WAP to search a value in a tuple using for loop and if else statement.

el_tup = (1,4,9,16,25,36,49,64,81,100)

find = int(input("Enter the value you want to find:"))

for x in el_tup:
    if(x == find):
        print('value found in tuple')
        break
else:
    print('value not found')

# WAP to print the numbers from 1 to 100 using for loop.
for y in range(1, 101):
    print(y) 

# WAP to print the numbers from 100 to 1 using for loop.
for z in range(100, 0, -1):
    print(z) 

# WAP to print the multiplication table of a number using for loop.
mul = int(input("Enter a value you want to write the table for:"))
for c in range(1,11):
    print(mul*c)

