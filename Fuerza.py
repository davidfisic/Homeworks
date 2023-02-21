# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:20:49 2023

@author: sebas
"""

class Fuerza:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        
        return("("+str(self.x)+","+str(self.y)+","+str(self.z)+")")
        
    def suma (self,otro):
        sum_x = self.x + otro.x 
        sum_y = self.y + otro.y
        sum_z = self.z + otro.z
        return (Fuerza (sum_x,sum_y,sum_z))
    
    def vectorial (self,otro):
        prod_vect_x = self.y*otro.z - otro.y*self.z
        prod_vect_y = self.x*otro.z - otro.x*self.z
        prod_vect_z = self.x*otro.y - otro.x*self.y
        return(Fuerza (prod_vect_x, prod_vect_y, prod_vect_z))
    
    def escalar (self,otro):
        producto_punto = self.x*otro.x + self.y*otro.y + self.z*otro.z
        return(producto_punto)
    
    def resta (self,otro):
        rest_x = self.x - otro.x
        rest_y = self.y - otro.y
        rest_z = self.z - otro.z
        return(Fuerza(rest_x,rest_y,rest_z))

p_1_x = "digite la posición inicial en x: "
p_1_y = "digite la posición inicial en y: "
p_1_z = "digite la posición inicial en z: "

pos_1_x = float(input(p_1_x))
pos_1_y = float(input(p_1_y))
pos_1_z = float(input(p_1_z))

posicion_1 =(Fuerza(pos_1_x,pos_1_y,pos_1_z))

p_2_x = "digite la posición final en x: "
p_2_y = "digite la posición final en y: "
p_2_z = "digite la posición final en z: "

pos_2_x = float(input(p_2_x))
pos_2_y = float(input(p_2_y))
pos_2_z = float(input(p_2_z))

posicion_2 =(Fuerza(pos_2_x,pos_2_y,pos_2_z))

desplazamiento = (posicion_2.resta(posicion_1))

print(desplazamiento)

F_x = "Escriba el valor de la fuerza en x: "
F_y = "Escriba el valor de la fuerza en y: "
F_z = "Escriba el valor de la fuerza en z: "

Fuerza_x = float(input(F_x))
Fuerza_y = float(input(F_y))
Fuerza_z = float(input(F_z))
Fuerza_ejercida = (Fuerza(Fuerza_x,Fuerza_y,Fuerza_z))

W = Fuerza_ejercida.escalar(desplazamiento)

trabajo = "El trabajo es: "
print(trabajo,W,"J")





