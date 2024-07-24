palindromo = input("Ingrese una palabra: ")
palabrainvertida=palindromo[::-1]

if palindromo==palabrainvertida:
    print("Es un palindromo")
else:
    print("No es un palindromo")