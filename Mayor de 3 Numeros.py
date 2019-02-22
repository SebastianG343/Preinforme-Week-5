lal=int(input("Digite el primer numero"))
lel=int(input("Digite el segundo numero"))
lil=int(input("Digite el tercer numero"))
if lal>lel>lil or lal>lil>lel:
    print(lal,"Es mayor a",lel,"Y",lil)
elif lel>lal>lil or lel>lil>lal:
    print(lel,"Es mayor a",lal,"Y",lil)
elif lil>lel>lal or lil>lal>lel:
    print(lil,"Es mayor a",lal,"Y",lel)
