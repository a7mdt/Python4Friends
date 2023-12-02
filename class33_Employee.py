class Employee:
# 33) init ==> initilaize .
    def __init__(self, name, age, department, isManager, rating, salary):
        self.name = name
        self.age = age
        self.department = department
        self.isManager = isManager
        self.rating = rating # from 1 to 5
        self.salary = salary

# 34) Put functions
    def isExcellent(self):
        if self.rating >= 4.5:
            return True
        else:
            return False

    def bonusLvL(self):
        if self.age >= 40 and self.age <= 60:
            return "U HAVE GOT BONUS", self.salary+500
        else:
            return "U R HERE so U DONT GET ANY BONUS"


