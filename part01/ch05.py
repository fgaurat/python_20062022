from collections import deque

l = [1,5,78,95]

l.append(78)
print(l)
nb = l.count(78)
print(nb)
print(l)
last_value = l.pop()
print(l)
print("last_value",last_value)
l.insert(0,12)
print(l)
last_value = l.pop(0)
print(l)
print(50*"-")
d = deque(l)
print(d)
d.appendleft(12)
print(d)
last_value = d.popleft()
print(last_value)
print(d)


print(50*'-')

l=[]
for i in range(1,5):
    l.append(i*2)
print(l)

l = [i*2 for i in range(1,5)]

l = list(map(lambda i:i*2,range(1,5)))
print(l)

l = [i*2 for i in range(1,5)]
print(l)

s = "   toto   "
print(s.strip(),len(s.strip()))

lines = ["ligne 01 ","   ligne 02  ","ligne 03  "," ligne 04    "]
clean_lines = []
for line in lines:
    clean = line.strip()
    clean_lines.append(clean)
print(clean_lines)


clean_lines = [line.strip() for line in lines]
print(clean_lines)

labels = ['name','firstname','job']
values = ['GAURAT','Fred','dev']

# name : GAURAT
# firstname : Fred
# job : dev


for i in range(len(labels)):
    print(labels[i],values[i])

for d in zip(labels,values):
    print(* d)

print(50*'-')


a,b=0,1

a,b,*c = 0,1,3,5,8,89,56,8,8


print(a,b)
print(c)

print(50*'-')
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

if 'apple' in basket:
    print("ok")



tel = {'jack': 4098, 'sape': 4139}

print(tel['jack'])

for k in tel:
    print(k,tel[k])

for k,v in tel.items():
    print(k,v)