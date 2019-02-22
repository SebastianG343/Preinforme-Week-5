n=int(input("Digite un numero para saber si es chevere"))
if n>5000:
    print(n,"No es chevere")
    if n>100:
        if  n%2!=0 and n%7!=0 and n%5==0:
            print(n,"Es chevere super chevere")
else:
    if n%2==0 and n>0 and n%7!=0 and n%9!=0:
        print(n,"Es chevere")
    else:
        print("No es chevere")
