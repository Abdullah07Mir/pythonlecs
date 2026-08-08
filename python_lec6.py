# WAF to print the length of a list. ( list is the parameter)


# list = [1,5,3,7,8,2,9]
# g_fact= 1

# def cal_len(n):
#     return len(n)

# print("Length of list is:", cal_len(list))

#  WAF to print the elements of a list in a single line. ( list is the parameter)
# print('Elements of the list')
# def print_elements(n):
#     for i in list:
#         print(i, end= " ")

# print_elements(list)

# print(end= "\n")
# print('Function for Factorial')
# def fact_fxn(n):
#     fact = 1
#     for i in range(1, n):
#         fact*= i
   
#     return fact

# g_fact=fact_fxn(5)

# print(g_fact)


# def sum_fxn(n):
#     if(n == 0):
#         return 0
#     return sum_fxn(n-1) + n 
   
# print(sum_fxn(5))


# def print_num(n): 5,4,3,2,1
#     if(n==0):
#         return 0
#     print_num(n-1)
#     print(n)
#     print('end')


# print_num(5)

# [1,5,3,7,8,2,9]
def print_list(list, indx):
    if(indx == len(list)):
        return 0
    print(list[indx])
    print_list(list, indx+1)
  


print_list([1,5,3,7,8,2,9], 0)


x= 0

def print_glob(y):
    z= x+y
    return z

a = print_glob(4)
print('xsacsca', a)
print(x)