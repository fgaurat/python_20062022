# from random import randint


# good_value = randint(10,500)

# user_value = int(input("Please enter an integer: "))


# while user_value != good_value:
#     if good_value>user_value:
#         print("plus")
#     else:
#         print("moins")
#     user_value = int(input("Please enter an integer: "))

# print("bravo !")

print(50*'-')

for i in range(5):
    print(i)

l = ['value 01','value 02','value 03','value 04']
for i in range(len(l)):
    print(str(i)+" "+l[i])
# 0 : value 01
# 1 : value 02
# 2 : value 02
# 3 : value 03

print(list(range(5)))

for indice,valeur in enumerate(l):
    print(str(indice)+" "+valeur)

l = [2,5,9,10]
print(sum(l))
found = False
for i in l:
    print(i)
    if i == 9:
        found=True
        print('ok')
        break

if found:
    print("valeur 9 dans la liste")
else:
    print("valeur 9 pas dans la liste")


for i in l:
    print(i)
    if i == 99:
        break
else:
    print("Valeur non présente")

for num in range(2, 10):
    if num % 2 == 0:
        print("Pair", num)
        continue
    print("Impair", num)


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end='-')
        a, b = b, a+b
    print()

def fib2(n=12):    # write Fibonacci series up to n
    """Return a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    
    return result

# Now call the function we just defined:
l = fib2()
print(l)
# l => [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]

l = fib2(4)


def say_hello(first_name="toto",name="TUTU"):
    result = "Hello "+first_name+" "+name+" !"
    return result

h = say_hello("Fred",'Gaurat') # Hello Fred Gaurat !
print(h)
h = say_hello()
print(h)
h = say_hello(first_name="Fred",name="Gaurat")
print(h)

h = say_hello('Gaurat',"Fred") # Hello Fred Gaurat !
print(h)

h = say_hello(name="Gaurat",first_name="Fred")
print(h)



def add(*the_list):
    result =0
    for v in the_list:
        result+=v

    return result

# l = [1,2,358,78]
# c = add(l)
# print(c)

c = add(1,3)
print(c)
c = add(1,3,5)
print(c)
c = add(1,3,5,89)
print(c)
c = add(1,3,5,89,789)
print(c)

def say_hello(**data):
    a = "toto" 
    print(data['first_name'])
    print(data['name'])
    print(data['job'])
    # result = "Hello "+first_name+" "+name+" !"
    # return result


h = say_hello(first_name="Fred",name="Gaurat",job="dev")
print(50*'-')


def add(*the_list)->int:
    """ sum all values of the list
    """
    result =0
    for v in the_list:
        result+=v

    return result


l = [1,2,35,8]

print(l) # [1,2,35,8]
print(1,2,35,8) #
add(*l)


def join(*row):
    result = ""
    for data in row:
        result+=str(data)+";"
    
    return result

row = ['GAURAT','Fred',45,'dev']

r = join('GAURAT','Fred',45,'dev')
print(r)
r = join(*row)
print(r)

# join(row) => GAURAT;Fred;45;dev








