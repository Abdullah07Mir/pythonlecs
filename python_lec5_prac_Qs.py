# WAP to find the sum of n numbers using while loop.
n = int(input("Enter total values you want sum for:"))
sum =0
i=1
while i<n:
    sum = sum+i
    i+=1
print("Sum after adding i in existing total is :", sum)

print("end of the program")

# WAP to find the factorial of n numbers.
x = int(input("Enter total values you want factorial for:"))
fac = 1
for a in range(1,x+1):
    fac = fac*a
print("fac of x values :", fac)
print("end of the program")

