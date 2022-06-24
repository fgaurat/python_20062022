notes = [10, 15, 5, 18]
print(notes[2])
print(notes)
somme_notes = 0

for n in notes:
    somme_notes = somme_notes+n
         
    print(n)


moyenne = somme_notes/len(notes)
print(len(notes))
print(moyenne)

print(somme_notes)
print("après la boucle")


print(50*"-")
somme_notes = 0
cpt = 0
for n in notes:
    if n % 2==0 :
        somme_notes = somme_notes+n
        cpt+=1

moyenne = somme_notes/cpt
print(moyenne)

a = 2
b = "toto"
# c = str(a)+b
c = a*b

print(c)

print(50*'-')


salut = "Bonjour"
hello = "Bonjour"
for c in salut:
    print(c)

print(id(salut))
print(id(hello))
hello = "Hello"
print(id(salut))
print(id(hello))
print(50*'-')
print(id(salut))
 
