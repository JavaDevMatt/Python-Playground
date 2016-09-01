class Employee:
    empCount = 0

    def __init__(self, name="Some Default Dude", salary=0):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def display_count():
        print("Total Employee %d" % Employee.empCount)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

print(50*"-")

e1 = Employee("Don Juan", 15000)
e1.display_count()
e1.display_employee()

print(50*"-")

e2 = Employee()
e2.display_count()
e2.display_employee()

print(50*"-")


