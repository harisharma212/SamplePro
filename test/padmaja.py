'''def myfun(*x):
	print(x)
	print(type(x))


myfun()
myfun(1,2)

def myfun(a,d,b=0,*c):
    print(a,b,c,d)

myfun(10,80,100,60)

def myfun(**x):
	print(x)

myfun()
myfun(a=10)

def myfun(a,b,c=10,*d,**e):
	print(a,b,c,d,e)






myfun(10,20)
myfun(10,20,30,40,50)	
myfun(10,20,30,40,x=10,y=10)


l = [1,8,2,6,7,4]

def even(a):
	# return a % 2 == 0
	if a%2 != 0:
		return a * a

print(list(filter(even,l)))


l=[1,8,2,7,4,6]
output = []

for  i in l:
	output.append(i*i+1)

print(output)

l=[1,2,3,4,5,6]

def square(r):
	op = r*r*r
	return op

print(list(map(square,l)))

'''

'''class MyClass:
		x = 10
		y = 20

obj = MyClass()
obj.y = 100
print(obj.y)

Class MyClass:
       x = 10
       y = 20

obj = MyClass()
obj.z = 40
prit(obj.z)
'''


'''
	y = 20

     
obj = A()
print(obj._A__x)
del obj.y
'''

def add(a,b,s = 10):
	return a+b+s

print(add(10,20))

def add(a,b):
	return a+b

def add(a,b):
	return a * b

print(add(10,20))

class A:
	def add(self,a,b):
		return a + b


class B:
	def add(self,a,b):
		return a * b

obj_a = A()
obj_b = B ()
print(obj_a.add(10,20))
print(obj_b.add(10,20))

class A:
	def add(self,a,b):
		return a - b
class B:
	def add(self,a,b):
		return a % b
obj = A()
obj = B()
print(obj)
print(obj.add(20,10))
print(obj.add(20,10))



