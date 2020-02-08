#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:09:50 2020

@author: MPAZ

toma la lista de pares con volatilidad y muchas ordenes y lo graba en un csv


"""

import shelve
from datetime import date

obj=shelve.open('tablas')

keys=list(obj.keys())

fecha=date.today()


pares=obj['pares_vivos']

largo=len(pares)

try:
    file=open('pares.csv','a')
    file.write(str(fecha)+','+str(largo)+',')
    for par in pares:
        file.write(par+',')
    file.write('\n')
    file.close()
    print('Vamos a seguir con el fichero')
except:
    
    file=open('pares.csv','w')
    file.write(str(fecha)+','+str(largo)+',')
    for par in pares:
        file.write(par+',')
    file.close()
    print('es nuevo el fichero generado pares.csv')
    
print('he llegado vivo al final del script')


# FALTA BLOQUE TRY EXCEPT
