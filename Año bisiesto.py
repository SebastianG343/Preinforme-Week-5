year=int(input("Digite un año para saber si es bisiesto"))
if year%4==0 and year%100:
    print("Nice",year,"es bisiesto")
else:
    print("Nope",year,"no es bisiesto")
