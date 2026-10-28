import string
import sys
from random import choice
from os import system
def palabras_random():
    lista_palabras = ["perro","gato","jirafa","leon","aguila"]
    return choice(lista_palabras)



def seleccion_letra():
    letra = " "
    while letra not in (string.ascii_letters):
        letra = input("Introduce una letra: ")
    return letra

def tablero_letra(palabra_secreta,letra_adivinada):
    guiones = 0
    for letra in palabra_secreta:
        if letra in letra_adivinada:
            print(letra,end=(" "))
        else:
            print("-",end=(" "))
            guiones += 1
    print()
    return guiones == 0


def juego():
    palabra_secreta = palabras_random()
    letras_acertadas = []
    letras_falladas = []
    vidas = 6
    print("ADIVINA LA PALABRA")
    tablero_letra(palabra_secreta, letras_acertadas)
    while vidas > 0:
        print(f"Le quedan {vidas} vidas")

        letra = seleccion_letra()
        if letra in letras_acertadas:
            print("Ya adivinaste esa letra")
            #tablero_letra(palabra_secreta, letras_acertadas)


        elif letra not in palabra_secreta:
            letras_falladas.append(letra)
            print(f"Esa letra no esta, estas son las letras falladas{letras_falladas} ")
            vidas -= 1
            #tablero_letra(palabra_secreta, letras_acertadas)


        elif letra in palabra_secreta:
            letras_acertadas.append(letra)
            print("Esa letra si esta")
            if tablero_letra(palabra_secreta,letras_acertadas):
                print("Ganaste")
                return


    if vidas == 0:
        print("Perdiste")

juego()

