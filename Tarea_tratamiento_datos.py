# -*- coding: utf-8 -*-
"""
Created on Fri May 19 23:52:17 2023

@author: sebas
"""

import pandas as pd

import numpy as np

class trat_dat:
    
    def __ini__ ():
        pass
    def leer (self):
        return pd.read_csv("survey_lung_cancer.csv",sep=",")
    def tabla (self):
        mensaj_1 = "Hola usuario esta es una base de datos sobre el\
            CANCER DE PULMÓN"
        return mensaj_1, self.leer()
    def info (self):
        mensaj_2 = "Estas son las columnas y el tipo de datos que contienen:"
        print(mensaj_2)
        return self.leer().info()
    def cols_num(self):
        cn = self.leer().select_dtypes(include=[int, float]).columns.tolist()
        for i,columna in enumerate(cn):
            print(i + 1,columna)
        index_selec = int(input("seleccione indice de la columna: ")) - 1
        return self.leer()[cn[index_selec]]
    def cols_str(self):
        cs = self.leer().select_dtypes(include=[object]).columns.tolist()
        for i,columna in enumerate(cs):
            print(i + 1,columna)
        index_selec = int(input("seleccione indice de la columna: ")) - 1
        return self.leer()[cs[index_selec]]
    def dat_unique(self):
        return np.sort(pd.unique(self.leer()[self.cols_num().name]))
    def filtro(self):
        for i,dato in enumerate(self.dat_unique()):
            print(dato)
        dat = eval(input("seleccione un dato "))
        return self.leer().loc[self.leer()[self.cols_num().name]==dat]
    
    
        
# df = db.loc[db["AGE"] ==valor]
x = trat_dat()

print(x.filtro())

# print(pd.unique(db["AGE"]))



        
