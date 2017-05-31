# Variable and Common Data Structure
a = 5
b = 5.0
c = 4
text = "HellO worlld"
flag = True
cities = ['delhi','jaipur','mumbai']
statement = "This is India"
output1 = "India is This"
output2 = "sihT si aidnI"

print(cities)

if a==4:
	print "4"
elif a>4:
	print ">4"
else:
	print "<4"


for i in range(12,2,-1):
	print i

for j in text[3:0:-1]:
	print j

for city in cities:
	print city

text2 = text[::-1]

print text2


#Duck Typing
def sum(a,b,c):
	return (a+b)*c

#print sum(cities,ci,5)

#string functions

print (text.lower())
print (text.upper())
print (text.title())
print (text.find('lll'))
print (text.replace('ll','yy'))
print (len(text.split('ll'))-1)
print (" ".join(cities))









