n1=float(int(input("Digite la N1")))
n2=float(int(input("Digite la N2")))
n3=float(int(input("Digite la N3")))
n4=float(int(input("Digite la N4")))
n5=float(int(input("Digite la N5")))
la_nota1=n1*0.10
la_nota2=n2*0.15
la_nota3=n3*0.25
la_nota4=n4*0.15
la_nota5=n5*0.35
lasnotas=la_nota1+la_nota2+la_nota3+la_nota4+la_nota5
if lasnotas>=3.0:
    print(f"Aprobo con",lasnotas)
    if lasnotas>=4.0:
        print(f"Felicitaciones, paso la materia con",lasnotas)
elif lasnotas<3.0:
    print(f"No aprobo con",lasnotas)
    if lasnotas>=2.0 and lasnotas<3.0:
        print(f"Desaprobo, sin embargo puede recuperar con",lasnotas)