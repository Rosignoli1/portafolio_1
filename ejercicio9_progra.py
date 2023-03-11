cade=input("Ingrese una palabra: ").lower()
cade2=cade[::-1]
if cade==cade2:
    print(f"{cade} es palindromo")
else:
    print(f"{cade} no es palindromo")
    
