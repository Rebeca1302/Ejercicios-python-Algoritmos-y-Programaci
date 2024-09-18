#Programa 

#Pedir al usuario que ingresé su evaluación

evaluacion = float(input("Ingrese su puntuación : "))
salario = 2400
#Verificar que la calificación esté en el rango de valores correcto
    #Si los puntos obtenidos son "0.0"

if 0.0 <= evaluacion <= 0.4:
        nivel_de_rendimiento = "Inaceptable"

    #Si los puntos obtenidos son "0.4"
elif  0.4 <= evaluacion <= 0.6:
        nivel_de_rendimiento = "Aceptable"

        #Si los puntos obtenidos son "0.6 o más"
elif  evaluacion >= 0.6 :
        nivel_de_rendimiento = "Meritorio"

else:
        #Se imprimirá un mensaje de error si la calificación no está en el rango de valores correctos
        print("Por favor, ingresa una calificación válida entre 0.0 y 1.0")

bonificacion = salario*evaluacion

    #Se imprimirá el resultado de la calificación correspondiente
print(f"Tu nivel de rendimiento ha sido: {nivel_de_rendimiento}")
print(f"Tu bonificacion: {bonificacion}€")
    

