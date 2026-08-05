# This is a simple python program to demonstrate the use of string functions
name = input("What is your name? ")
strLen= len(name)

print('Name you entered is:', name)
print('Length of the name is:', strLen)

#  find the number of occurences of a letter in a string
str = "Hi I am $ and my simbol is $ and worth is $99.99"
occurences = str.count('$')
print('Number of occurences of letter $ in the string is:', occurences)


# WAP if a number entered by user is even or odd 
num = int(input("ENter the number please:"))

if(num% 2 == 0):
    print("num is even ")
elif(num% 3 == 0):
    print("num is odd")
else:
    print("num is neither even nor odd")

print("end of the program")


# WAP to enter three numbers and find the greatest among them
print("You need to enter three values and we check which is greater among them")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

print('You entered:',a ,b ,c)

if(a>b and a>c):
    print(a, 'is greater')
elif(b>a and b>c):
    print(b, 'is greater')
else:
    print(c, 'is greater')