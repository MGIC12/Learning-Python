nombre = input("Hola buen día, ¿Cómo es su nombre? ")
print(f"Hola {nombre}! :D, "+"Buenos días? o Buenas noches?")
respuesta = input()
determinanteRespuesta = respuesta
if respuesta == "Buenos días" :
    determinanteRespuesta = True
else:
    determinanteRespuesta = False

if determinanteRespuesta == True :
    print("Buena respuesta!")
elif determinanteRespuesta == False:
    print("Mala respuesta :(")