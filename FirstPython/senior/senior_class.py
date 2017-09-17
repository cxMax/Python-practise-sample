# coding=utf-8
class Employee:
    count = 0
    name = 'default'
    salary = 'secret'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.count

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

    def __del__(self):
        print 'it has been deleted !'


employee = Employee('卢本伟', '牛逼')
employee.displayEmployee()
employee.displayCount()

print getattr(employee, 'name')

del employee

class SeniorEmployee(Employee) :
    level = 'manager'

    def __init__(self, level):
        self.level = level

    def displayCount(self):
        print 'this is children\'s displayCount'


senior = SeniorEmployee('boss')
senior.displayCount()
