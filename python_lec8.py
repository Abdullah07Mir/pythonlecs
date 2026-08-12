# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Student:
#     def __init__(self):
#         print("This system is for students")
#     def __init__(self, name, math_marks, phy_marks, chem_marks):
#         self.name = name
#         self.math_marks = math_marks
#         self.phy_marks = phy_marks
#         self.chem_marks = chem_marks
#     def cal_avg(self):
#         self.avg_marks = (self.math_marks+ self.phy_marks +self.chem_marks) /300
#         print('The avg marks of ',self.name, 'are: ',self.avg_marks)


# s1 = Student("Abdullah", 98 , 96, 81)
# s2 = Student("Saad", 98 , 96, 78)
# s3 = Student("Ali", 81 , 63, 52)

# s1.cal_avg()
# s2.cal_avg()
# s3.cal_avg()


class Account:
    def __init__(self, bal, acc_no):
        self.bal = bal
        self.acc_no = acc_no

    def debit(self, debitted):
        self.bal -= debitted
        print(debitted,"Rs are debitted from your account")   

    def credit(self, creditted):
        self.bal += creditted 
        print(creditted,"Rs are creditted into your account")

    def check_bal(self):
        print('The balance for account num:', self.acc_no, 'is: ', self.bal)

a1 = Account(50000, 1234)
a2 = Account(10000, 5678)
a1.check_bal()
a2.check_bal()
a1.debit(10000)
a2.credit(5000)
a1.check_bal()
a2.check_bal()