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

with open("practice.txt", "r+") as y:
    data_in_file = y.read()
    print(data_in_file)
    if("Java" in data_in_file):
        newdata_in_file= data_in_file.replace("Java","Python")
    y.seek(0)
    y.write(newdata_in_file)
    y.close()


with open("practice.txt", "r") as z:
    search_data = z.read()
    if("learning" in search_data):
        print("Found")
    else:
        print("Not found")
z.close()

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


with open("countFile.txt", "w")as c:
    c.write("1,2,5,4,6,3,7,8,9,12,10")
    c.close()

with open("countFile.txt", "r") as num:
    count_even = num.read()
    newcount_even = int(count_even)
    q = 0
    for v in newcount_even:
        if(v % 2 == 0):
            q+=1
    print("Count of even numbers in file are:", q )
    num.close()        


     