# -*- coding: utf-8 -*-
"""
Created on Mon Jun 02 09:55:14 2014

@author: i13392
"""

# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


obesoReg = namedtuple("obesoReg", "id, nome")
listaObesos = []



def encontrar_posicao(codigo):
    pos = -1
    for i in range (len(listaObesos)):
        if listaObesos[i].id == codigo:
            pos = i
            break
                            
    return pos


def inserir_obeso():
    cod = input("Qual o codigo? ")

    pos = encontrar_posicao(cod)

    if pos >= 0:
        print "Código já existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    
    registo = obesoReg(cod, nome)
    listaObesos.append(registo)


def pesquisar_obeso():
    cod = input("Qual o codigo do obeso a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe obeso com esse código"
        return

    print "Código: ", listaObesos[pos].id
    print "Nome: ", listaObesos[pos].nome
    


def listar_obeso():
    for i in range (len(listaObesos)):
        print "Código: ", listaObesos[i].id
        print "Nome: ", listaObesos[i].nome
        
  

def eliminar_obeso():
    cod = input ("Código do obeso a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe obeso com esse código"
        return

    # TODO: Confirmar eliminação
    listaObesos.pop(pos)


    
def alterar_obeso():
    cod = input ("Código do obeso a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "Não existe obeso com esse código"
        return

    # só altera o nome
    novonome = raw_input("Qual o nome? ")
    listaObesos[pos] = listaObesos[pos]._replace(nome=novonome)



        

def gerir():

    terminar = False

    while not terminar:
        op = menu.obeso()

        if op == '1':
            inserir_obeso()
        elif op =='2':
            listar_obeso()
        elif op == '3':
            pesquisar_obeso()
        elif op == '4':
            alterar_obeso()
        elif op == '5':
            eliminar_obeso()
        elif op == '0':
            terminar = True




if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"
