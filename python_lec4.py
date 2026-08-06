#  WAP to enter three favourite movie names and store them in a list and print the list

dict = {}
dict.update({
    "table":("a piece of furniture", "list of facts and figures"),
    "cat": "small animal"
})

print(dict)
print(type(dict))

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
sub = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(sub)
print(len(sub))

#  WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
sub_marks={}
chem = int(input("Enter marks of chemistry:"))
phy = int(input("Enter marks of physics:"))
maths = int(input("Enter marks of maths:"))
sub_marks.update({
    "chemistry": chem,
    "physics": phy,
    "maths": maths
})
print(sub_marks)

# Figure out a way to store 9 & 9.0 as separate values in the set.
set= set()

set.add(("int", 9))
set.add(("float", 9.0))

print(set)