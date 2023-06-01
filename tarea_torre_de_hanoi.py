# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:25:13 2023

@author: sebas
"""

def mov(n):
    if n == 1:
        return 1
    else:
        return 2 * mov(n-1) + 1

    
def hanoi(n, origen, auxiliar, destino):
    """
    Mueve n discos desde la torre origen hasta la torre destino
    utilizando la torre auxiliar como ayuda.
    """
    if n == 1:
        # Caso base: si solo hay un disco, lo movemos de origen a destino
        print(f"Mueve disco de la torre {origen} a la torre {destino}")
    else:
        # Paso recursivo: movemos n-1 discos de origen a auxiliar utilizando destino como ayuda
        hanoi(n-1, origen, destino, auxiliar)
        # Movemos el disco restante de origen a destino
        print(f"Mueve disco de la torre {origen} a la torre {destino}")
        # Movemos los n-1 discos que están en auxiliar a destino utilizando origen como ayuda
        hanoi(n-1, auxiliar, origen, destino)

"""Se pide al usuario ingresar el numero de discos, y medicante la función \
mov se imprimen los movimientos necesarios, luego se llama a la función \
hanoi para resolver paso por paso, donde imprime cada uno de los pasos. """

n = int(input("Ingrese el número de discos: "))
hanoi(n, "A", "B", "C")
movimientos = mov(n)
print("se hacen: {0} movimientos".format(movimientos))