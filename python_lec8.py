class Student:
    def __init__(self):
        print("This system is for students")
    def __init__(self, name, math_marks, phy_marks, chem_marks):
        self.name = name
        self.math_marks = math_marks
        self.phy_marks = phy_marks
        self.chem_marks = chem_marks
    def cal_avg(self):
        self.avg_marks = (self.math_marks+ self.phy_marks +self.chem_marks) /300
        print('The avg marks of ',self.name, 'are: ',self.avg_marks)


s1 = Student("Abdullah", 98 , 96, 81)
s2 = Student("Saad", 98 , 96, 78)
s3 = Student("Ali", 81 , 63, 52)

s1.cal_avg()
s2.cal_avg()
s3.cal_avg()
        
