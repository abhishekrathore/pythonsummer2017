class Word:
	name = "abc"
	wordlist =[]
	def __init__(self,name):
		self.name=name
		self.wordlist=[]

	def add(self,item):
		self.wordlist.append(item)


w1 = Word("xyz")
w2 = Word("abc")

w1.add("a")
w2.add("b")
w1.add("c")

print w1.wordlist
print w2.wordlist
print w1.name
print w2.name

w1=w2

print w1.name
w1.name = "xyz"
print w2.name
w2.name  = "cde"
print w1.name





