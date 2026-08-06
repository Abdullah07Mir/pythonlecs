# #  WAP to enter three favourite movie names and store them in a list and print the list 
movie_list = []
movie1 = input("Enter your first fav movie name:")
movie2 = input("Enter your second fav movie name:")
movie3 = input("Enter your third fav movie name:")

movie_list.append(movie1)
movie_list.append(movie2)
movie_list.append(movie3)
print("Your favourite movies are:", movie_list)

# WAP to check if a list is palindrome or not

list1 = [1,2,3,2,1]
list2=  list1.copy()
list2.reverse()
print("list2 is:", list2)
if(list2 == list1):
    print("list is palindrome")
else:
    print("list is not palindrome")

print("end of the program")

# WAP to find the number of occurences of a letter in a tuple and sort the tuple
tup = ("C", "D", "A", "A", "B", "B","A")
print("Number of occurences of A in the tuple is:", tup.count("A"))

# WAP to sort the tuple and print the sorted list
list1 = list(tup)
list1.sort()
print("Sorted list is:", list1) 