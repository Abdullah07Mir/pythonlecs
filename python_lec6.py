# WAF to print the length of a list. ( list is the parameter)


list = [1,5,3,7,8,2,9]
g_fact= 1

def cal_len(n):
    return len(n)

print("Length of list is:", cal_len(list))

#  WAF to print the elements of a list in a single line. ( list is the parameter)
print('Elements of the list')
def print_elements(n):
    for i in list:
        print(i, end= " ")

print_elements(list)

print(end= "\n")
print('Function for Factorial')
def fact_fxn(n):
    fact = 1
    for i in range(1, n):
        fact*= i
   
    return fact

g_fact=fact_fxn(5)

print(g_fact)




