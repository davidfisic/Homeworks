# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:42:16 2023

@author: sebas
"""

k=9E9

class Campo:
    def __init__(self,x,y,z,q=0):
        self.x=x
        self.y=y
        self.z=z
        self.carga=q
        
    def __add__(self,otro):
        suma=Campo(self.x+otro.x,self.y+otro.y,self.z+otro.z)
        return(suma)
    
    def __sub__(self,otro):
        resta=Campo(self.x-otro.x,self.y-otro.y,self.z-otro.z)
        return(resta)
    
    def Norma(self,otro):
        resta=(self-otro)
        n=((resta.x)**2+(resta.y)**2+(resta.z)**2)**0.5
        return(n)
    
    def campo(self,otro):
        Ex=k*(self.carga/((self.Norma(otro))**2))*(((self.x-otro.x)**2)**0.5)
        Ey=k*(self.carga/((self.Norma(otro))**2))*(((self.y-otro.y)**2)**0.5)
        Ez=k*(self.carga/((self.Norma(otro))**2))*(((self.z-otro.z)**2)**0.5)
        return(Campo(Ex, Ey, Ez))
    
    def __str__(self):
        
        return("("+str(self.x)+","+str(self.y)+","+str(self.z)+")")

camp_1 =Campo(1,2,3,8)

camp_2 =Campo(9,2,4,6)

camp_3 =Campo(5,8,9)

print(camp_1.campo(camp_3))