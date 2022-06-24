from Carre import Carre
from Rectangle import Rectangle
from Cercle import Cercle


def affiche_surface(o):
    print(o.calc_surface(),o)

def main():
    r = Rectangle(2,5)
    r1 = Rectangle(2,5)
    c = Carre(2)

    affiche_surface(r)
    affiche_surface(c)
    
    #if r.__eq__(r1):
    if r==r1:
        print("ok")
    else:
        print("ko")
    
    print("calc_surface",r.calc_surface())

    ce = Cercle(12)
    print(ce.calc_surface())

    # print(c.cote)  
    # print(c.get_surface())  
    # c.cote = 10 
    # print(c.cote)  
    # print(c.get_surface())  
    # print(c)
    # print(50*'-')
if __name__ == "__main__":
    main()