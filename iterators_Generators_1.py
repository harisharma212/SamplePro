'''
Iterators:
---------
* Iterators are special data structures in Python, Which can handle one element 
  at a time from given data.

* Which avoids unnecessary memory consumption.

* It will be useful when we are working with large amount 
  of data files or data structures.

Syntax:
-------
	iterator_name = iter(Group_Of_Elements)

* The output format is always an iteator_object.

# To access the data from the iterator object, Use the below syntax.

Syntax:
------
	next(iterator_name)
'''


my_iterators = iter([8, 9, 3, 4, 52, 1])
print(my_iterators) # <list_iterator object at 0x000001D7715012A0>
print(next(my_iterators)) # 8 # The memory allocation will not happen, until you cal next method.
print(next(my_iterators)) # 9
print(next(my_iterators)) # 3

print("HELLOOOOOOO")
# print(next(my_iterators)) # StopIteration (When we process all the elements)

# try to use for loop to access the data from an iterator.

'''
Cons:
-----
* We can't control the data to be inserted into the iterator object.
# Iteration Control Behavior is achievable in Iterators.
'''

'''
Generators:
----------
* Generators will also works like iterators. (All generators are iterators.)
   (Once the generator is created, it will work like iterator.)

* To create a generator use the combination of a function along with "yield" keyword.

Syntax:
-------

def function_name(*args, **kwargs):
	statement - 1
	stetemnet - 2
	...
	yield "DATA"


generaor_name = funciton_name(Values...)
'''

def getInfo(l):
	for i in l:
		if i % 3 == 0:
			yield i

# When the yield keyword executed for the first time, It'll create a generator object,
# And the data associated with yield will insert into the generator.
# And it'll wait for the others elements in the loop to be processed.
# Once all the elements processed, it will return GENERATOR_OBJECT to the calling function.

x = getInfo([1, 2, 3, 4, 5])
print(x)

for i in x:
	print(i)

# return vs Yield
# iterator vs Generator
