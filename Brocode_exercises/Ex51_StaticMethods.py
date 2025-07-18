"""
Static Methods - A method that belong to a class rather than any object from that class (instance)
Usually used for general Utility functions

Instance methods - Best for operations on instance of the class(objects)
Static Methods - Best for utility functions that do not need access to class data
"""

class Employee:

    def __init__(self,employee_name,employee_position):
        self.employee_name = employee_name
        self.employee_position = employee_position

    def get_info(self):
        return f"{self.employee_name} : {self.employee_position}" # -- Instance Method

    @staticmethod
    def valid(position):
        valid_position = ["Manager","TL","Ass.Manager","Trainee"]
        return position in valid_position
employee1 = Employee("Kumar","Manager")
print(Employee.valid("Manager"))
print(employee1.get_info())