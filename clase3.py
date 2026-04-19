nombre = input("Ingrese solo primer nombre: ")
apellido = input("Ingrese primer apellido: ")
edad = input("Ingrese edad: ")
correo = input("ingrese correo electronico: ")

print("==========================================")
if nombre.isalpha():
    print("Nombre: \t\t", nombre)
else:
    print("ERROR con el nombre")

if apellido.isalpha():
    print("Apellido: \t\t", apellido)
else:
    print("ERROR con el apellido")

if edad.isdigit() and int(edad) >= 18:
    print("Edad: \t\t\t", edad)
else:
    print("ERROR con tu edad, no eres mayor de edad o has ingresado un parametro incorrecto")
if "@" in correo:
    print("Correo electronico: \t", correo)
else:
    print("ERROR con el correo")

print("==========================================")
if (nombre.isalpha()) and (apellido.isalpha()) and (edad.isdigit() and int(edad) >= 18) and ("@" in correo):
    print("Puedes inscribirte en el club, pero deberás renovar tu membresía en 3 años")
    print("Así que recuerda, cuando tengas", int(edad) + 3, "años, deberás renovarlo")
    print("==========================================")