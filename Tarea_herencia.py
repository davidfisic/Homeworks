# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:11:36 2023

@author: sebas
"""

import random

class R2:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def __getitem__(self,i):
        comp = [self.x,self.y]
        if i<1 or i>2:
            return "indice incorrexto"
        else:
            return comp[i-1]     
    def __add__ (self,otro):
        return R2(self.x + otro.x,self.y + otro.y)
    
    def __sub__(self,otro):
        return R2(self.x - otro.x,self.y - otro.y)
    def __str__(self):
        return("("+str(self.x)+","+str(self.y)+")")
    def sum_cuad(self):
        return(self.x**2 + self.y**2)
    def magnitud(self):
        return(self.sum_cuad()**(1/2))
    def __mul__(self,otro):
        return(self.x*otro.x + self.y*otro.y)
    def vect_al(self):
        return(R2(random.randint(0,100),random.randint(0, 100)))
    
class R3(R2):
    
    def __init__(self,x=0,y=0,z=0):
        super().__init__(x,y)
        self.z = z
    def __str__(self):
        return super().__str__()[:-1] + "," + str(self.z)+")"
    def __add__(self,otro):
        return R3(self.x + otro.x,self.y + otro.y,self.z + otro.z)
    def __sub__(self,otro):
        return R3(self.x - otro.x,self.y - otro.y,self.z - otro.z)
    def __getitem__(self,i):
        comp = [self.x,self.y,self.z]
        if i<1 or i>3:
            return "indice incorrexto"
        else:
            return comp[i-1] 
    def sum_cuad(self):
        return super().sum_cuad() + self.z**2
    def magnitud(self):
        return(self.sum_cuad()**(1/2))
    def __mul__(self,otro):
        return(super().__mul__(otro) + self.z*otro.z)
    def vect_al(self):
        return R3(random.randint(0,100),random.randint(0, 100),
                  random.randint(0,100))

x = R3()

print(x.vect_al())

