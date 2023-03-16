print("--------------------------------------")
print("-------PIEDRA, PAPEL O TIJERA---------")
print("--------------------------------------")

print("1. PIEDRA")
print("2. PAPEL")
print("3. TIJERAS")

# input 
import random
bandera = False 
user= int(input("seleccione una opcion: "))
piedra = 1
papel = 2
tijeras = 3
p = "piedra"
pa = "papel"
t = "tijeras" 
computer = random.randint(1,3)

#procesing
if user== 1 and computer == 1:
    option=p
    optionpc=p
    rta = ("EMPATADO")
elif user == 2 and computer == 2:
    option=pa
    optionpc=pa
    rta = ("EMPATADO")
elif user == 3 and computer ==3:
    option=t
    optionpc=t
    rta = ("EMPATADO")
elif user == 1:
    option=p
    if computer == 2:
        optionpc=pa
        rta = ("GANADO")
    else:
        optionpc=t
        rta = ("PERDIDO")
elif user == 2:
    option=pa
    if computer == 1:
        optionpc=p
        rta = ("GANADO")
    else:
        optionpc=t
        rta = ("PERDIDO")
elif user == 3:
    option=t
    if computer == 1:
        optionpc=p
        rta = ("PERDIDO")
    else:
        optionpc=pa
        rta = ("GANADO")
else :
    bandera = True

# output
print("-----------------------------")
print("----------RESULTADOS---------")
print("-----------------------------")

if bandera == False:
    print("HAZ: ", rta)
    print("opcion del user ==>",str(option))
    print("opcion del computer ==>",str(optionpc))
else:
    print("No has ingresado una opcion válida")

