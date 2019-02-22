fondos=3000000
caso1=5000
caso2=10000
caso3=20000
caso4=50000
caso5=100000
caso6=150000
caso7=200000
caso8=250000
caso9=300000
caso10=350000
caso11=400000
menu=(" ")
while menu!=("1000"):
    yorn=""
    print("¡Hola usuario! sus fondos son: 3.000.000")
    while yorn!="Si" and yorn!="No":
        if fondos<=0:
            print("Ella no te ama :'v")
        while fondos>0:
            yorn=input("¿Va a retirar cantidades mayores a $150.000? R= Si//No")
            if yorn!="Si" and yorn!="No":
                print("Pls my friend: Digite ¨Si¨ o ¨No¨ >:v")
            if yorn=="No":
                money=""
                while money!="1" and money!="2" and money!="3" and money!="4" and money!="5" and money!="6":
                    print("/1=$5.000/2=$10.000/3=$20.000/4=$50.000/5=$100.000/6=$150.000")
                    money=input("Digite la opción que indica cuanto dinero va a retirar")
                    if money!="1" and money!="2" and money!="3" and money!="4" and money!="5" and money!="6":
                        print("Pls my dude: No se haga el genio")
                    if money=="1":
                        fondos-=caso1
                        print("Usted a retirado",caso1,"sus fondos son",fondos)
                        print(" *Le da un billete de 5.000 xD*")
                    if money=="2":
                        fondos-=caso2
                        print("Usted a retirado",caso2,"sus fondos son",fondos)
                        print(" *Le da un billete de 10.000 xD*")
                    if money=="3":
                        fondos-=caso3
                        print("Usted a retirado",caso3,"sus fondos son",fondos)
                        print("* Le da un billete de 20.000 xD*")
                    if money=="4":
                        fondos-=caso4
                        print("Usted a retirado",caso4,"sus fondos son",fondos)
                        print("* Le da un billete de 50.000 xD*")
                    if money=="5":
                        rcaso5=caso5/caso4
                        fondos-=caso5
                        print("Usted a retirado",caso5,"sus fondos son",fondos)
                        print("* Le da",rcaso5,"billetes de",caso4,"*")
                    if money=="6":
                        rcaso6=caso6/caso4
                        fondos-=caso6
                        print("Usted a retirado",caso6,"sus fondos son",fondos)
                        print("* Le da",rcaso6,"billetes de",caso4,"*")
            elif yorn=="Si":
                monhe=""
                while monhe!="1" and monhe!="2" and monhe!="3" and monhe!="4" and monhe!="5" and monhe!="6":
                    print("/1=$200.000/2=$250.000/3=$450.000/4=$600.000/5=$700.000/6=$800.000")
                    monhe=input("Digite la opción que indica cuanto dinero va a retirar")
                    if monhe!="1" and monhe!="2" and monhe!="3" and monhe!="4" and monhe!="5" and monhe!="6":
                        print("Plx my dude: No te hagas el 100tifiko")
                    if monhe=="1":
                        rcaso7=caso7/caso4
                        fondos-=caso7
                        print("Usted a retirado",caso7,"sus fondos son",fondos)
                        print("* Le da",rcaso7,"billetes de",caso4,"*")
                    if monhe=="2":
                        rcaso8=caso8/caso4
                        fondos-=caso8
                        print("Usted a retirado",caso8,"sus fondos son",fondos)
                        print("* Le da",rcaso8,"billetes de",caso4,"*")
                    if monhe=="3":
                        rcaso9=caso11+caso4
                        divcaso9=rcaso9/caso4
                        fondos-=rcaso9
                        print("Usted a retirado",rcaso9,"sus fondos son",fondos)
                        print("* Le da",divcaso9,"billetes de",caso4,"*")
                    if monhe=="4":
                        rcaso10=caso9+caso9
                        divcaso10=rcaso10/caso4
                        fondos-=rcaso10
                        print("Usted a retirado",rcaso10,"sus fondos son",fondos)
                        print("* Le da",divcaso10,"billetes de",caso4,"*")
                    if monhe=="5":
                        rcaso11=caso9+caso11
                        divcaso11=rcaso11/caso4
                        fondos-=rcaso11
                        print("Usted a retirado",rcaso11,"sus fondos son",fondos)
                        print("* Le da",divcaso11,"billetes de",caso4,"*")
                    if monhe=="6":
                        rcaso12=caso11+caso11
                        divcaso12=rcaso12/caso4
                        fondos-=rcaso12
                        print("Usted a retirado",rcaso12,"sus fondos son",fondos)
                        print("* Le da",divcaso12,"billetes de",caso4,"*")