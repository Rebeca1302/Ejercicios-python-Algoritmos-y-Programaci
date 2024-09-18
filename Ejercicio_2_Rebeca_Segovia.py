#programa que calcule el área de un rectángulo e indique si el área es mayor a 40 y su altura es mayor a 10 muestre un mensaje personalizado en pantalla 

#Pedir al usuario que ingrese la base del rectángulo
b = float(input("Ingrese la base del rectángulo: "))

#Pedir al usuario que ingrese la altura del rectángulo
h = float(input("Ingrese la altura del rectángulo: "))

#Operacion para calcular el área del rectángulo
a = b * h

#Mostrar el área calculada
print(f"El área del rectángulo es: {a}")

#Si las condiciones se cumplen se mostrará un mensaje personalizado
if a > 40 and h > 10:
    print("Me sorprendes bro, sabia que llegarias muy lejos.... mentira, no sabia :p, pero que bueno es Dios")

#Si no se cumplen, no imprimirá ningún mensaje
else:
    print("")
