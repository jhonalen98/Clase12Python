NumeroTemperaturas=int(input("Ingrese cuantas temperaturas desea ingresar: "))
ListaTemperatura=[]

for C in range (NumeroTemperaturas):
    temperatura=float(input(f"Ingrese la temperatura numero {C+1}: "))
    ListaTemperatura.append(temperatura)

suma=sum(ListaTemperatura)
media=suma/NumeroTemperaturas
contador=0

for temperatura in ListaTemperatura:
    if temperatura >= media:
        contador +=1

print(f"La media de las temperaturas es {media}")
print(f"las temperaturas que superan la media son {contador}")