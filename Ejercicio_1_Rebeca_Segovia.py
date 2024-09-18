## Programa para preguntar al ususraio su nombre y edad, y saber si es o no mayor de edad
#Le pregunto al usuario su nombre utilizando la funcion input

nombre = input ("¿Como te llamas bro?")
#Le pregunto al usuario su edad utilizando la funcion input
edad = int ( input ("¿Que edad tiene bro?") )
#utilizando if le esplicamos al programa la primera condicion 
if edad >= 18:
    print ( f"Wao bro, eres mayor de edad bro, {nombre}")

#utilizando else le explicamos al programa que si no se cumple la primera condicion entonces imprimira un mensaje para indicar que no se cumplio

else:
    print (f"Que decepcion bro, todavia eres un bebe {nombre}")
