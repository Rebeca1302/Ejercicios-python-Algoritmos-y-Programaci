#Programa que pida al usuario una calificación (0-100) y muestre por pantalla la calificación correspondiente

#Pedir al usuario que ingresé su calificación
calificacion = float(input("Ingresa una calificación (0-100): "))

#Verificar que la calificación esté en el rango de valores correcto
if 0 <= calificacion <= 100:

    #Si la calificación está entre el rango "90/100"
    if 90 <= calificacion <= 100:
        letra = 'A'

    #Si la calificación está entre el rango "80/89"
    elif 80 <= calificacion < 90:
        letra = 'B'

    #Si la calificación está entre el rango "70/79"
    elif 70 <= calificacion < 80:
        letra = 'C'

    #Si la calificación está entre el rango "60/69"
    elif 60 <= calificacion < 70:
        letra = 'D'

        #Si la calificación está entre el rango "0/59"
    else:
        letra = 'F'

    #Se imprimirá el resultado de la calificación correspondiente
    print(f"La calificación correspondiente es: {letra}")
    
else:
    
    #Se imprimirá un mensaje de error si la calificación no está en el rango de valores correctos 
    print("Por favor, ingresa una calificación válida entre 0 y 100.")
