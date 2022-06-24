def main():
    
    name ="Fred GAURAT"
    age = 45

    # format string
    hello = f"Bonjour {name} age : {age}"

    # par position
    hello = "Bonjour {0} age : {1}".format(name,age)
    
    # par keywords
    hello = "Bonjour {nom} age : {age}".format(nom = name,age = age)

    print(hello)


    data = ["Fred GAURAT",45]
    hello = "Bonjour {0} age : {1}".format(*data)
    print("*",hello)
    
    data ={
        "name":"Fred GAURAT",
        "age":45
    }
    hello = "Bonjour {name} age : {age}".format(**data)


    a = 2
    b = 3
    c = a/b
    result = f"{a}/{b} = {c*100:.2f}%"
    result = f"{a}/{b} = {c:.2%}"
    print(result)

if __name__ == "__main__":
    main()