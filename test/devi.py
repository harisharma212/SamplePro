l=["hi", "hello", "world"]
res =[]
for s in l:
	res.append(s[::-1])

print(res)


data ='''name1 banglore IBM 1000 
name2 chennai infoysis 2000'''


op = {}

for row in data.splitlines():
	name, loc, comp, sal = row.split()
	op[name] =  [loc, comp, sal]

print(op)
	

