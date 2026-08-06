#  WAP to enter three favourite movie names and store them in a list and print the list

# dict = {}
# dict.update({
#     "table":("a piece of furniture", "list of facts and figures"),
#     "cat": "small animal"
# })

# print(dict)
# print(type(dict))

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# set = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(set)
# print(len(set))


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