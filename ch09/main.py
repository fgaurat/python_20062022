



from Rectangle import Rectangle


def main():
    r = Rectangle(10,12) # longueur = 10, largeur = 12
    r1 = Rectangle(1,2)
    r2 = Rectangle(21,52)

    print(Rectangle.cpt)
    # assert r.get_longueur() == 10
    # print(r.get_longueur()) #  10 ?
    # print(r.get_largeur()) #  12 ?
    # r.set_longueur(100)
    # print(r.get_longueur()) #  100 ?
    # r.set_largeur(20)
    # print(r.get_largeur()) #  20 ?

    # s = str(r)
    # print(s)
    # a = int(r)
    # print(a)

if __name__ == "__main__":
    main()