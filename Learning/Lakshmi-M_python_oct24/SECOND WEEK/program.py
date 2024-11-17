class Student:
    pass
class Employee:
    pass
class Manager(Employee):
    pass
class Director(Manager):
    pass
print(issubclass(Director, Employee)) # True
print(issubclass(Manager, Employee))  # True
print(issubclass(Manager, Director))  # False
print(issubclass(Director, Manager))  # True
print(issubclass(Director, Director)) # True
employee = Employee()
manager = Manager()
print(isinstance(manager, Manager))
print(isinstance(manager, Employee))
print(isinstance(employee, Manager))



#class Student(object):
class Student:
    student_count = 0
    student_id = 101
    def __init__(self, name = 'mahesh'):
        self.__id = Student.student_id
        self.__name = name
        Student.student_count += 1
        Student.student_id += 1
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    @classmethod
    def get_student_count(cls):
        return Student.student_count
        # return cls.number_of_students
    def __str__(self):
        return f'Id={self.__id}, Name={self.__name}'
s1 = Student()
s2 = Student('Girish')
s3 = Student('Satish')
#print(dir(Student))
print(s1) # calls the implicit method __str__()
#print('Student1 name is', s1.name) # error
print('Student1 name is', s1.get_name()) 
print('Student1 id is', s1.get_id()) 
#print(dir(s1))
print(getattr(s1, 'branch', 'CSE')) # To temporarily add a new attribute to the object
print(s1) 

#class Student(object):
class Student:
    student_count = 0 
    student_id = 101
    def __init__(self, name = 'mahesh'):
        self.__id = Student.student_id
        self.__name = name
        Student.student_count += 1
        Student.student_id += 1
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    @classmethod
    def get_student_count(cls):
        return Student.student_count
        # return cls.number_of_students
    def __str__(self):
        return f'Id={self.__id}, Name={self.__name}'
s1 = Student()
print('Student Count now is', Student.get_student_count())
s2 = Student('Girish')
s3 = Student('Satish')
s4 = Student('Lakshmi')
print('Student Count now is', Student.student_count)
print(f'Student1 details are: {s1}')
print(f'Student2 details are: {s2}')
print(f'Student3 id is', s3.get_id())
print(f'Student3 name is', s3.get_name())
print(f'Student4 details are: {s4}')

class MyClass:
    class_var = 1
    
    @classmethod
    def class_method(cls):
        MyClass.class_var += 1
        return cls.class_var
    
    @staticmethod
    def static_method():
        MyClass.class_var += 1
        return f"This is a static method {MyClass.class_var}"
		
    @staticmethod
    def another_static_method():
        MyClass.class_var += 1
        return f"This is a static method {MyClass.class_var}"
        
print(MyClass.class_method())  # Output: 2
print(MyClass.static_method())
print(MyClass.another_static_method())
print(MyClass.class_method())

class Employee:
	id = 101
	def __init__(self, name, designation, salary):
		self.id = Employee.id
		self.name = name
		self.designation = designation
		self.salary = salary
		Employee.id += 1
	def __str__(self):
	    return f'{self. id}, {self.name}, {self.designation}, {self.salary}'
class Manager(Employee):
    def __init__(self, name, designation, salary, commission):
            super().__init__(name, designation, salary)
            self.commission = commission
    def __str__(self):
		    return f'{self.id}, {self.name}, {self.designation}, {self.salary}, {self.commission}'
emp1 = Employee('asha', 'developer', 125000)
m1 = Manager('lakshmi', 'manager', 325000,2500)
emp2 = Employee('usha', 'developer', 225000)
print(emp1)
print('emps :',emp2)
print(m1)
emp2 = m1
print('emps :',emp2)