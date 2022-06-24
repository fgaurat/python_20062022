a = "L'orage gronde"
print(a)
a = 'L\'orage gronde'
print(a)
a = "il a dit :\"l'orage gronde\""
print(a)
a = "il a dit \n:\"l'orage gronde\""
print(a)
p = "c:\\newdocuments\\thedocument.pdf"
p = r"c:\newdocuments\thedocument.pdf"
print(p)

a = """ligne 1
ligne 2
ligne 3
"""
print(a)

s = "bonjour"
pos = len(s)-1 # 7-1 
print(s[pos])  #r
print(s[len(s)-1])  #r
print(s[-1])  #r

print(s[2:5])
print(s[0:3])
print(s[:3])
print(s[3:])

print(s)
s = "L"+s[1:]
print(s)
print(50*'-')
squares = [1, 4, 9, 16, 25]
squares2 = squares[:]
squares[0] = 1000
print(squares)
print(squares2)


l = [
    [10,20],
    [30,40],
    [50,60]
]

l2 = l[:]
l[0][1] = 1000
print(l2)
print(50*'-')
l = [10,20,30,40]

for n in l:
    print(n)

n=0
while n<len(l):
    print(l[n]) 
    n+=1

print(50*'-')

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b