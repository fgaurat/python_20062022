import traceback
from DivBy12Error import DivBy12Error



def division(a,b):
    if b==12:
        err = DivBy12Error()    
        raise err
        
    r = a/b
    return r


def call_divi(a,b):
    r= 0
    try:
        r = division(a,b)
    finally:
        print("fin de call_divi")
    return r
    
def main():

    try:
        a=2
        b=int(input('valeur de b : '))
        c = call_divi(a,b)
        print(c)

    except ZeroDivisionError as e:
        print('ZeroDivisionError !')
        print(e)
        traceback.print_exc()
    # except ValueError as e:
    #     print('ValueError !')
    #     print(e)
    except Exception as e:
        print('Exception !')
        print(e)
        traceback.print_exc()
    else:
        print("pas d'erreurs !!!")

    print("fin du script")

if __name__ == "__main__":
    main()