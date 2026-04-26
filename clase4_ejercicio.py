nombre = input("Ingrese su nombre: ").strip()

if nombre.isalpha():
    print("Ingresaste tu nombre correctamente!")
else:
    print("ingresaste mal el nombre")
    nombre = input("Ingrese su nombre: ").strip()
    if nombre.isalpha():
        print(f"Nombre:  {nombre.title()}")
    else:
        print("otra vez ingresaste mal el nombre")


apellido = input("ingrese su apellido: ")


if apellido.isalpha():
    print("Ingresaste tu apellido correctamente!")
else:
    print("ingresaste mal tu apellido")
    apellido = input("Ingrese su apellido: ").strip()
    if apellido.isalpha():
        print("ingresaste bien tu appelido")
    else:
        print("otra vez ingresaste mal tu apellido")


edad = input("Ingrese su edad ")



correo = input("ingrese su correo: ").strip()
if correo.count("@") != 1:
    print("Ingresaste mal, el correo debe tener ""@"" ")

    


print ("============================================================")

if nombre.isalpha():
    print(f"Nombre:  {nombre.title()}")
else:
    print("Nombre: ingresaste mal el nombre, deberás hacer todo otra vez")



if apellido.isalpha():
    print(f"Apellido:  {apellido.title()}")
else:
    print("Apellido: ingresaste mal el apellido, deberás hacer todo otra vez")


if edad.isdigit():   #Acá pregunto si el valor ingresado es un numero
    edad_numero = int(edad)          #Si lo es lo pasa a valor entero y comienza un nuevo if comparando esa nueva variable con ese valor ingresado
    if edad_numero <= 15:
        print(f"Edad: {edad} eres menor de edad")
    elif edad_numero < 18:
        print(f"Edad: {edad} eres adolecente menor de edad")
    elif edad_numero >= 18:
        print(f"Edad: {edad} eres adulto mayor de edad")
else:
    print("ingresaste mal la edad")    #Pero si no puso un numero...


if correo.count("@") != 1:
    print("Ingresaste mal, el correo debe tener ""@"" ")
else:
    print(f"Correo:  {correo}")
