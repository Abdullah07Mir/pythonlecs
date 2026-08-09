#  Create a new file “practice.txt” using python. Add data in it:

f = open("practice.txt", "w")
f.write("Hi everyone \n")
f.close()

x = open("practice.txt", "a+")
x.write("We are learning File I/O \n")
x.write("using Java. \n")
x.write("I like programming in Java. \n")
x.seek(0)
data= x.read()
print("...", data)
x.close()

# WAF that replace all occurrences of “java” with “python” in above file.
with open("practice.txt", "r+") as y:
    data_in_file = y.read()
    print(data_in_file)
    if("Java" in data_in_file):
        newdata_in_file= data_in_file.replace("Java","Python")
    y.seek(0)
    y.write(newdata_in_file)
    y.close()

# Search if the word “learning” exists in the file or not.
with open("practice.txt", "r") as z:
    search_data = z.read()
    if("learning" in search_data):
        print("Found")
    else:
        print("Not found")
z.close()

# WAF to find in which line of the file does the word “learning”occur first. Print -1 if word not found.
with open("practice.txt", "r") as a:
    i = 0
    line = a.readline()
    while  line!= "":
        if("learning" in a.readline()):
            print("Found learning in line number :", i)
            break
        else:
            line = a.readline()
            i+=1
    print("Not Found at any line")

a.close()

# From a file containing numbers separated by comma, print the count of even numbers.
with open("countFile.txt", "w")as c:
    c.write("1,2,5,4,6,3,7,8,9,12,10")
    c.close()

with open("countFile.txt", "r") as num:
    count_even = num.read()
    print("the data in file is", count_even)
    newcount_even  = list(count_even.split(','))
    new_list = [int(x) for x in newcount_even]
    q = 0
    for v in new_list:
        if(v % 2 == 0):
            q+=1
    print("Count of even numbers in file are:", q )
    num.close()        



     