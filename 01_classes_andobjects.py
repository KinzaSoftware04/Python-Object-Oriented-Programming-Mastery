class Student:
    def __init__(self , name ,roll_no):
        self.name = name
        self.roll_no = roll_no
    def introduce(self):
        print(f"Student  Name is {self.name} and roll_no is {self.roll_no}")
s1 = Student("Kinza" , 101)
s2 = Student("sana",102)
s1.introduce()
s2.introduce()





