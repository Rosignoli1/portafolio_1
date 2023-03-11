c1=input("Ingrese el primer caracter: ")
c2=input("Ingrese el segundo caracter: ")
cade=input("Ingrese una cadena de caracteres: ")
cade2=""

for x in cade:
    if x==c1:
        cade2+=c2
    else:
        cade2+=x
print(cade2)
