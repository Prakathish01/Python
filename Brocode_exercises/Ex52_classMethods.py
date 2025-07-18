"""
class methods - Allow operations related to the class itself
                Take (cls) as the first parameter , which represents the class itself
"""
class Students:
    count = 0
    def __init__(self,name,height):
        self.name = name
        self.height = height
        Students.count += 1
    def get_score(self):
        return f"{self.name} : {self.height} feet"

    @classmethod
    def student_count(cls):
        return Students.count

student1 = Students("Sundar",5.4)
print(student1.get_score())
print(Students.student_count())

