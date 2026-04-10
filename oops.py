class Student():
	def __init__(self, name, marks1, marks2, marks3):
		self.name = name
		self.marks1 = marks1
		self.marks2 = marks2
		self.marks3 = marks3

	def avg(self, marks1, marks2, marks3):
		print((marks1+marks2+marks3)/3)

s1 = Student("Megha",1, 2, 3)
s1.avg(100,99,99)