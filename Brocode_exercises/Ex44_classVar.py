# Class variable
# -> Shared among all instances of a class
# -> defined outside the constructor
# -> Allow you to share data among all objects created from that class


class Student:
    count =0  #--------- class variables
    class_ = "10-A" #--------- class variables
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        Student.count += 1
student1 = Student("Kumar","69")
student2 = Student("senthil","70")
student3 = Student("velu","71")

print(f"The {Student.class_} class has {Student.count} students.")



