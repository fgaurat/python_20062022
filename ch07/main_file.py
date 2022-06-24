def main():
    with open('mon_fichier.txt','w',encoding="UTF-8 ") as f:
        for i in range(100):
            print(i,"Une ligne dans le fichier avec print !",file=f)
            print(i,"Une deuxième ligne dans le fichier avec print !",file=f)
    
    with open('mon_fichier.txt','r',encoding="UTF-8 ") as f:
        # l = f.readlines()
        # print(l)
        for line in f:
            print(line.strip())
        


if __name__ == "__main__":
    main()