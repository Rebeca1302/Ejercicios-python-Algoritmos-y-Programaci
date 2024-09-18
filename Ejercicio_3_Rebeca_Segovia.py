# Programa que pregunte al usuario por la contraseña e imprima si la contraseña introducida coincide con la guardada en la variable 

#Pedir al usuario que cree su contraseña
contraseña = input ("Ingrese su contraseña")

#Informar al usuario que la contraseña fue guardada exitosamente
print ("Su contraseña fue guardada")


#Pedirle que ingrese su contraseña 
print ("Ingrese nuevamente su contraseña")

#Si la contraseña es correcta, imprimirá un mensaje que valide el acceso 
if input () == contraseña:
    print ("La contraseña es correcta bro, puedes pasar adelante :3")

#Si la contraseña no es correcta, imprimirá un mensaje que niegue el acceso
else:
    print ("La contraseña ta' mala bro, no podes pasar :(")
