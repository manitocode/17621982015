# coding=UTF-8

class SchoolMember(object):
	'''代表学校里的任何成员'''
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print('(Initialized SchoolMember: {})'.format(self,name))

	def tell(self):
		print('Name:"{}"" Age:"{}"'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary = salary
		print('Initialized Teacher:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('salary is "{:d}"'.format(self.salary))

class Student(SchoolMember):
	"""docstring for Student"""
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized Student:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('marks is "{:d}"'.format(self.marks))

t = Teacher('Ms zhou',24,15000)
s = Student('Ms wang',23,75)

print()
members = [t, s]
for member in members:
	member.tell()
