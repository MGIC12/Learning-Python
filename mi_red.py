print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

#Primera interacción. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

#Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. ¿Por qué decimos que solo estamos "estimando" su edad?
#¿Qué ocurre si eliminamos la conversión a tipo de dato 'int' de la siguiente lí­nea?
agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2024-agno-1
print()

#Tercera interacción. Solicitamos la estatura, medida en metros.
#Utilizamos la conversión a 'int', y una expresión para convertir esto
#a una medida en metros y centímetros
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dá­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interacción. Consultamos cuántos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

#Quinta interacción. Se consulta el género/sexo del usuario.
genero = input("Menciona tu género/sexo. ")

#Sexta interacción. Se solicita el país de nacimiento.
pais_nac = input("¿En qué país naciste? ")

#Séptima interacción. Preguntamos por el número de teléfono.
num_telefono = input("Número de teléfono: ")

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centí­metros")
print("Amigos:  ", num_amigos)
print("Género/Sexo:  ", genero)
print("País de nacimiento:  ", pais_nac)
print("Número de teléfono:  ", num_telefono)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Usaremos una variable bool para indiciar si el usuario dewsea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecucion hasta que el usuario desee salir
while continuar:
    escribir_mensaje = str(input("¿Desea escribir un mensaje? (S/N)"))
    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    elif escribir_mensaje == "N" or escribir_mensaje == "n":
        continuar = False