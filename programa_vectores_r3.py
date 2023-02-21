# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:53:51 2023

@author: sebas
"""

class Vector_R3 :
    def __init__(self,X,Y,Z=0):
        self.x = X
        self.y = Y
        self.z = Z
        self.magnitud = (self.x**2 + self.y**2 + self.z**2)**0.5
        
    def __str__(self):
        
        return("("+str(self.x)+","+str(self.y)+","+str(self.z)+")")

    def suma (self,otro):
        sum_x = self.x + otro.x 
        sum_y = self.y + otro.y
        sum_z = self.z + otro.z
        return (Vector_R3 (sum_x,sum_y,sum_z))
    
    def resta (self,otro):
        rest_x = self.x - otro.x
        rest_y = self.y - otro.y
        rest_z = self.z - otro.z
        return(Vector_R3(rest_x,rest_y,rest_z))
    
    def escalar (self,otro):
        producto_punto = self.x*otro.x + self.y*otro.y + self.z*otro.z
        return(producto_punto)
    
    def vectorial (self,otro):
        prod_vect_x = self.y*otro.z - otro.y*self.z
        prod_vect_y = self.x*otro.z - otro.x*self.z
        prod_vect_z = self.x*otro.y - otro.x*self.y
        return(Vector_R3(prod_vect_x, prod_vect_y, prod_vect_z))
    
    
    
x = Vector_R3(4,7)

y = Vector_R3(-3,7)

print(x.vectorial(y))
        
