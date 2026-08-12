# WAP 
# class Circle:
#     def __init__(self, radius):
#         self.radius =  radius

#     def area(self):
#         self.area = 3.14* self.radius**2
#         return self.area
#     def  parameter(self):
#         self.parameter = 2*3.14*self.radius
#         return self.parameter
# c1 = Circle(21)
# print("The area of the circle is :", c1.area())
# print("The parameter of the circle is :", c1.parameter())

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary =  salary

    def show_details(self):
        
        print("Role: ", self.role, "\n", "Department: ", self.department, "\n", "Salary: ", self.salary )

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Data Scientist", "Tech", 60000)

    def output(self):
        print("__Employee details__")
        print("Name: ",self.name, "\n", "Age: ", self.age)
        super().show_details()

e1 = Engineer("Abdullah Mir", 25)
e1.output()
        