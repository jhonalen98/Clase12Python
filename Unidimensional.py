#Declarar una lista unidimensional de frutas
frutas=["Pera", "Manzana", "Piña", "Fresa"]
print(frutas)

#Permite agregar elementos .append
frutas.append("Melon")

print(frutas)

#Acceder a elemento de la lista (arreglo unidimensional)
print(frutas[4])

frutas[4]="Arandano"
print(frutas[4])

#Ejercicio de Ordenamiento .sort
digitos=[5,2,1,0,3,6,7,8,9]
print(digitos)

digitos.sort()
print(digitos)

digitosCero=5*[0]
print(digitosCero)

print(frutas)

#Ejercicio de tamaño de la lista
print("Cantidad de frutas ingresadas: ", len(frutas))