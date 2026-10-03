class Student:
    university_name = "IUB"
    def __init__(self , name ,roll_no):
            self.name = name
            self.roll_no = roll_no  
    def check_result(self, marks):
        self.marks  = marks
        if marks >= 80:
            print(f"{self.name} is passed with {marks} from{self.university_name}")
        else:
            print(f"{self.name} is failed  with {marks} from{self.university_name}") 
    def print_report_card(self):
         print(f"-----Report Card:{self.name} Scored {self.marks} marks-------- ")
s1 = Student("sana" , 101)  
s2 = Student("hina" , 202)
s1.check_result(90)
s2.check_result(34)
s1.print_report_card()
s2.print_report_card()