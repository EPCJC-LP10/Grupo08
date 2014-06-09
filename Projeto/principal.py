# -*- coding: utf-8 -*-
"""
Created on Mon Jun 02 09:51:01 2014

@author: i13392
"""

# -*- coding: utf-8 -*-

import menu
import Obesos
import util


# nome dos ficheiros
fxObesos = "fxObesos.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	Obesos.listaAlunos = util.ler_ficheiro(fxObesos)


def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxObesos, Obesos.listaObesos)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()
    
    if op == '1':
        Obesos.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()
