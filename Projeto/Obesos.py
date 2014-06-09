# -*- coding: iso8859-1 -*-
"""
Created on Mon Jun 02 09:55:14 2014

@author: i13392
"""

# -*- coding: utf-8 -*-

from collections import namedtuple

import menu


obesoReg = namedtuple("obesoReg", "id, nome, telefone")
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
        print "C�digo j� existe"
        return

    #ler dados
    nome = raw_input("Qual o nome? ")
    telefone = raw_input("Qual o telefone? ")
    
    registo = obesoReg(cod, nome, telefone)
    listaObesos.append(registo)


def pesquisar_obeso():
    cod = input("Qual o codigo do obeso a pesquisar? ")

    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe obeso com esse c�digo"
        return

    print "C�digo: ", listaObesos[pos].id
    print "Nome: ", listaObesos[pos].nome
    print "Telefone: ", listaObesos[pos].telefone
    


def listar_obeso():
    for i in range (len(listaObesos)):
        print "C�digo: ", listaObesos[i].id
        print "Nome: ", listaObesos[i].nome
        print "Telefone: ", listaObesos[pos].telefone
        
  

def eliminar_obeso():
    cod = input ("C�digo do obeso a eliminar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe obeso com esse c�digo"
        return

    # TODO: Confirmar elimina��o
    listaObesos.pop(pos)


    
def alterar_obeso():
    cod = input ("C�digo do obeso a alterar --> ")
    pos = encontrar_posicao(cod)

    if pos == -1:
        print "N�o existe obeso com esse c�digo"
        return

    # s� altera o nome
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
    print "Este programa n�o deve ser executado diretamente"
