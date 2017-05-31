class Polygon:
	name="polygon"
	area =0
	x = 1
	y = 2
	def __init__(self,name):
		self.name = name

	def area(self):
		return 1

class Surface:
	name="Surface"

	def __init__(self,name):
		self.name = name

	def area(self):
		return 2



class Square(Surface,Polygon):
	name="Square"
	def __init__(self,name):
		Polygon.__init__(self,name)





p1 = Polygon('triangle')
s1 = Square('sq')
print s1.area()
print p1.name
print s1.name
