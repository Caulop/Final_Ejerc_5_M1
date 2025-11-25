"""Ejercicio 5 
Enunciado: 
Crea un programa que lea la edad de una persona y determine si puede votar 
(mayor o igual a 18 años), si debe presentar tarjeta de identidad (entre 7 y 17 años), 
o si es menor para tener documento
"""
print("***********************************")
print("*** Bienvenido al Validador de ****")
print("************  Votación  ***********")
print("***********************************")
print("")
print ("Porfavor Ingrese Su Nombre:")
nombre = input ()
print ("Porfavor Ingrese Su Apellido:")
apellido = input()
print("")
nombre_competo = nombre + " " + apellido

while True:
    print(" ")
    print("****************************************")
    print("Gracias Por Visitarnor:", nombre_competo)
    print("****************************************")
    print("")
    print("Seleccione la opción que quieres o vuelva a intentarlo.")
    print("1: Vota Por Primera Vez")
    print("2: Ya Has Votado")
    print("3: Salir Del Validador")

    respuesta = int (input ())


    if respuesta == 1:
        edad = int(input("Opcion 1:Ingrese su edad:",))
        print("")
        if edad >=18:
            print("***********************************")
            print("Opcion 1:Puedes Votar:", nombre_competo)
            print("***********************************")
        elif 7 <= edad <= 17:
            print("************************")
            print("Opcion 1:Debes presentar tarjeta de identidad, ", nombre_competo)
            print("************************")
        else:
            print("************************************")
            print("Opcion 1:Es menor de edad no puedes votar", nombre_competo)
            print("************************************")
    elif respuesta == 2:
        print("*************************************")
        print("Opcion 2:Ya has votado, ", nombre_competo)
        print("*************************************")
    elif respuesta == 3:
        print("***********************************")
        print("Opcion 3:hasta luego", nombre_competo)
        print("***********************************")
        break