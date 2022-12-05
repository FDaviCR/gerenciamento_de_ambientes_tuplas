# Bibliotecas de uso geral
import sys
import os
import time, random

import linsimpy
# Bibliotecas para manipulação e construção da interface gráfica -----
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font

# Espaço de Tuplas
tse = None

# Lista que vai registrar o nome dos usuários criados e sua 'flags' de recebimento de novas msgs ('0' quando não detectou nenhuma msg nova e '1' quando detectou)
lista_registro_nuvens = []

'''
-----------------------------------------------------------------------------------------
--------------------------------- CRIAÇÃO DOS CONTEINER ---------------------------------
-----------------------------------------------------------------------------------------
'''
# Criação da Nuvem e das matrizes para armazenar as NUVENS
def criarNuvem(ts, nomeNuvem):
    initNuvem = []
    integrantes = []
    ts.out(("INTNUVEM", nomeNuvem, tuple(integrantes)))
    ts.out(("NUVEM", nomeNuvem, tuple(initNuvem)))

    nuvens = ts.inp(("NUVENS", object))
    temp = list(nuvens[1])
    temp.append(nomeNuvem)
    ts.out(("NUVENS", tuple(temp)))

# Criação do Host e das matrizes para armazenar os HOSTS
def criarHost(ts, nomeHost):
    initHost = []
    integrantes = []
    ts.out(("INTHOST", nomeHost, tuple(integrantes)))
    ts.out(("HOST", nomeHost, tuple(initHost)))

    hosts = ts.inp(("HOSTS", object))
    temp = list(hosts[1])
    temp.append(nomeHost)
    ts.out(("HOSTS", tuple(temp)))

# Criação do Host e das matrizes para armazenar os HOSTS
def criarVM(ts, nomeVM):
    initVM = []
    integrantes = []
    ts.out(("INTVM", nomeVM, tuple(integrantes)))
    ts.out(("VM", nomeVM, tuple(initVM)))

    vms = ts.inp(("VMS", object))
    temp = list(vms[1])
    temp.append(nomeVM)
    ts.out(("VMS", tuple(temp)))

# Cria a tupla do Processo e coloca ela na tupla 'PROCESSOS' para ser armazenada
def criarProcesso(ts, nomeProcesso):
    processos = ts.inp(("PROCESSOS", object))

    temp = list(processos[1])
    temp.append(nomeProcesso)
    ts.out(("PROCESSOS", tuple(temp)))

'''
-----------------------------------------------------------------------------------------
-------------------------------- LISTAGENS DE CONTEINERS --------------------------------
-----------------------------------------------------------------------------------------
'''
# Listar TODAS as NUVENS do 'ts' ('Tuple Space')
def listarNuvens(ts):
    nuvens = ts.rdp(("NUVENS", object))
    print(nuvens)
    
    return list(nuvens[1])

# Listar TODAS as HOSTS do 'ts' ('Tuple Space')
def listarHosts(ts):
    hosts = ts.rdp(("HOSTS", object))
    print(hosts)
    
    return list(hosts[1])

# Listar TODAS as VMS do 'ts' ('Tuple Space')
def listarVMs(ts):
    vms = ts.rdp(("VMS", object))
    print(vms)
    
    return list(vms[1])

# Listar TODAS as PROCESSOS do 'ts' ('Tuple Space')
def listarProcessos(ts):
    processos = ts.rdp(("PROCESSOS", object))
    print(processos)
    
    return list(processos[1])

'''
-----------------------------------------------------------------------------------------
------------------------ LISTAGENS DE INTEGRANTES DOS CONTEINERs ------------------------
-----------------------------------------------------------------------------------------
'''
# Lista integrantes de uma sala em específico 'nomeSala' 
def listarIntegrantesNuvem(ts, nomeNuvem):
    integrantes = ts.rdp(("INTNUVEM", nomeNuvem, object))
    print(integrantes)
    return list(integrantes[2])

# Lista integrantes de uma sala em específico 'nomeSala' 
def listarIntegrantesHost(ts, nomeHost):
    integrantes = ts.rdp(("INTHOST", nomeHost, object))
    print(integrantes)
    return list(integrantes[2])

# Lista integrantes de uma sala em específico 'nomeSala' 
def listarIntegrantesVM(ts, nomeVM):
    integrantes = ts.rdp(("INTVM", nomeVM, object))
    print(integrantes)
    return list(integrantes[2])

'''
-----------------------------------------------------------------------------------------
-------------------------------- ENTRADAS NOS CONTEINERS --------------------------------
-----------------------------------------------------------------------------------------
'''
# Add host na nuvem em que entrou
def entrarNuvem(ts, nome, nomeNuvem):
    integrantes = ts.inp(("INTNUVEM", nomeNuvem, object))
    temp = list(integrantes[2])
    temp.append(nome)
    ts.out(("INTNUVEM", nomeNuvem, tuple(temp)))
    print("Host: " + nome + "entrou na nuvem: " + nomeNuvem)
    
# Add vm no host em que entrou
def entrarHost(ts, nome, nomeHost):
    integrantes = ts.inp(("INTHOST", nomeHost, object))
    temp = list(integrantes[2])
    temp.append(nome)
    ts.out(("INTHOST", nomeHost, tuple(temp)))
    print("VM: " + nome + "entrou no host: " + nomeHost)

# Add processo no vm em que entrou
def entrarVM(ts, nome, nomeVM):
    integrantes = ts.inp(("INTVM", nomeVM, object))
    temp = list(integrantes[2])
    temp.append(nome)
    ts.out(("INTVM", nomeVM, tuple(temp)))
    print("Processo: " + nome + "entrou na VM: " + nomeVM)
    
'''
-----------------------------------------------------------------------------------------
-------------------------- SAIDAS DO CONTEINER DE INTEGRANTES ---------------------------
-----------------------------------------------------------------------------------------
'''
# Retira host da nuvem em que entrou
def sairNuvem(ts, nome, nomeNuvem):
    integrantes = ts.inp(("INTNUVEM", nomeNuvem, object))
    temp = list(integrantes[2])
    temp.remove(nome)
    ts.out(("INTNUVEM", nomeNuvem, tuple(temp)))
    
# Retira vm do host em que entrou
def sairHost(ts, nome, nomeHost):
    integrantes = ts.inp(("INTHOST", nomeHost, object))
    temp = list(integrantes[2])
    temp.remove(nome)
    ts.out(("INTHOST", nomeHost, tuple(temp)))

# Retira processo da vm em que entrou
def sairVM(ts, nome, nomeVM):
    integrantes = ts.inp(("INTNUVEM", nomeVM, object))
    temp = list(integrantes[2])
    temp.remove(nome)
    ts.out(("INTNUVEM", nomeVM, tuple(temp)))

'''
-----------------------------------------------------------------------------------------
-------------------------------- REMOVER DOS CONTEINERS ---------------------------------
-----------------------------------------------------------------------------------------
'''
# Retira a tupla do nuvem da tupla 'NUVENS' aonde foi armazenada
def deletarNuvem(ts, nome):
    nuvens = ts.inp(("NUVENS", object))
    temp = list(nuvens[1])
    print(temp)
    temp.remove(nome)
    ts.out(("NUVENS", tuple(temp)))

# Retira a tupla do host da tupla 'HOSTS' aonde foi armazenada
def deletarHost(ts, nome):
    hosts = ts.inp(("HOSTS", object))
    temp = list(hosts[1])
    print(temp)
    temp.remove(nome)
    ts.out(("HOSTS", tuple(temp)))

# Retira a tupla do vm da tupla 'VMS' aonde foi armazenada
def deletarVM(ts, nome):
    vms = ts.inp(("VMS", object))
    temp = list(vms[1])
    print(temp)
    temp.remove(nome)
    ts.out(("VMS", tuple(temp)))

# Retira a tupla do processo da tupla 'PROCESSOS' aonde foi armazenada
def deletarProcesso(ts, nome):
    processos = ts.inp(("PROCESSOS", object))
    temp = list(processos[1])
    print(temp)
    temp.remove(nome)
    ts.out(("PROCESSOS", tuple(temp)))

'''
-----------------------------------------------------------------------------------------
---------------------------- FUNÇÕES PARA TROCA DE MENSAGENS ----------------------------
-----------------------------------------------------------------------------------------
'''
# Add as mensagens a Lista de mensagens que a VM em específico do chat do processo possui
def mandarMensagem(ts, nomeVM, remetente, destinatario, mensagem):
    mensagens = ts.inp(("VM", nomeVM, object))
    temp = list(mensagens[2])
    temp.clear()
    
    temp.append((destinatario,"<" + remetente + ">: " + mensagem))
            
    ts.out(("VM", nomeVM, tuple(temp)))

# Retorna a ''última mensagem enviada'' no chat de Tuplas
def receberMensagem(ts, nomeVM):
    mensagens = ts.rdp(("VM", nomeVM, object))
    #print("Recebe MSG " + str(mensagens))
    return list(mensagens[2])

'''
-----------------------------------------------------------------------------------------
-------------------------------- MAIN PARA INICIALIZAÇÃO --------------------------------
-----------------------------------------------------------------------------------------
'''
if __name__ == "__main__":
    tse = linsimpy.TupleSpaceEnvironment()

    nuvens = []
    hosts = []
    vms = []
    processos = []

    tse.out(("NUVENS", tuple(nuvens)))
    tse.out(("HOSTS", tuple(hosts)))
    tse.out(("VMS", tuple(vms)))
    tse.out(("PROCESSOS", tuple(processos)))

    #root.mainloop()