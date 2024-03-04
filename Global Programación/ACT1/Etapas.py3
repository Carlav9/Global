***********
** Autor: Carla Julieta Valtierra Arguelles
** Fecha: 10/Feb/2024
** Trabajo: Etapas de la vida
**********

print("Dame una edad")
n = int(input())  # Para pedir una entrada puedes usar la función input()

def clasificar_edad(edad):  # Aquí debes usar la variable edad en lugar de L
    if edad>=0 and edad<=3:
        return "BEBE"
    elif edad<=4 and edad<=14:
        return "NIÑO"
    elif edad<=15 and edad<=18:
        return "JOVEN"
    elif edad<=19 and edad<=65:
        return "ADULTO"
    else:
        return "ADULTO 3RA"

clasificacion = clasificar_edad(n)
print(clasificacion)  # Aquí debes usar la función print() para imprimir la clasificación
