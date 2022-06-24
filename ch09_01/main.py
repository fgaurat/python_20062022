



from Rectangle import Rectangle
 

def main():
    r = Rectangle(10,12) # longueur = 10, largeur = 12
    
    r.longueur = 12
    r.largeur = 22
    print(r.longueur)
    print(r.largeur)

if __name__ == "__main__":
    main()