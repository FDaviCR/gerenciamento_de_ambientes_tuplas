# Bibliotecas de uso geral
import sys
import os
import time, random
import tkinter as tk

import linsimpy
# Bibliotecas para manipulação e construção da interface gráfica -----

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font

# Espaço de Tuplas
tse = None

# Lista que vai registrar o nome dos usuários criados e sua 'flags' de recebimento de novas msgs ('0' quando não detectou nenhuma msg nova e '1' quando detectou)
lista_registro_processos = []

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
    lista_temp = [nomeProcesso,0]
    lista_registro_processos.append(lista_temp)

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
    
    return list(nuvens[1])

# Listar TODAS as HOSTS do 'ts' ('Tuple Space')
def listarHosts(ts):
    hosts = ts.rdp(("HOSTS", object))
    
    return list(hosts[1])

# Listar TODAS as VMS do 'ts' ('Tuple Space')
def listarVMs(ts):
    vms = ts.rdp(("VMS", object))
    
    return list(vms[1])

# Listar TODAS as PROCESSOS do 'ts' ('Tuple Space')
def listarProcessos(ts):
    processos = ts.rdp(("PROCESSOS", object))
    
    return list(processos[1])

'''
-----------------------------------------------------------------------------------------
------------------------ LISTAGENS DE INTEGRANTES DOS CONTEINERs ------------------------
-----------------------------------------------------------------------------------------
'''
# Lista integrantes de uma sala em específico 'nomeSala' 
def listarIntegrantesNuvem(ts, nomeNuvem):
    integrantes = ts.rdp(("INTNUVEM", nomeNuvem, object))

    return list(integrantes[2])

# Lista integrantes de uma sala em específico 'nomeSala' 
def listarIntegrantesHost(ts, nomeHost):
    integrantes = ts.rdp(("INTHOST", nomeHost, object))

    return list(integrantes[2])

# Lista integrantes de uma sala em específico 'nomeSala' 
def listarIntegrantesVM(ts, nomeVM):
    integrantes = ts.rdp(("INTVM", nomeVM, object))

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
    
# Add vm no host em que entrou
def entrarHost(ts, nome, nomeHost):
    integrantes = ts.inp(("INTHOST", nomeHost, object))
    temp = list(integrantes[2])
    temp.append(nome)
    ts.out(("INTHOST", nomeHost, tuple(temp)))

# Add processo no vm em que entrou
def entrarVM(ts, nome, nomeVM):
    integrantes = ts.inp(("INTVM", nomeVM, object))
    temp = list(integrantes[2])
    temp.append(nome)
    ts.out(("INTVM", nomeVM, tuple(temp)))
    
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
    integNuvem = listarIntegrantesNuvem(tse, nome)
    
    if(len(integNuvem) == 0):
        nuvens = ts.inp(("NUVENS", object))
        temp = list(nuvens[1])
        temp.remove(nome)
        ts.out(("NUVENS", tuple(temp)))
    else:
        janelaConteinerNaoVazio()

# Retira a tupla do host da tupla 'HOSTS' aonde foi armazenada
def deletarHost(ts, nome):
    integHost = listarIntegrantesHost(tse, nome)
    if(len(integHost) == 0):
        hosts = ts.inp(("HOSTS", object))
        temp = list(hosts[1])

        temp.remove(nome)
        ts.out(("HOSTS", tuple(temp)))
    else:
        janelaConteinerNaoVazio()

# Retira a tupla do vm da tupla 'VMS' aonde foi armazenada
def deletarVM(ts, nome):
    integVM = listarIntegrantesVM(tse, nome)
    
    if(len(integVM) == 0):
        vms = ts.inp(("VMS", object))
        temp = list(vms[1])

        temp.remove(nome)
        ts.out(("VMS", tuple(temp)))
    else:
        janelaConteinerNaoVazio()

# Retira a tupla do processo da tupla 'PROCESSOS' aonde foi armazenada
def deletarProcesso(ts, nome):
    processos = ts.inp(("PROCESSOS", object))
    temp = list(processos[1])

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
def recebeMensagem(ts, nomeVM):
    mensagens = ts.rdp(("VM", nomeVM, object))
    
    return list(mensagens[2])

'''
-------------------------------------------------------------------------------------------------
---------------------------------- CONSTRUÇÃO DA INTERFACE GRAFICA ------------------------------
-------------------------------------------------------------------------------------------------
'''

root = Tk()
root.withdraw()

def fecharAplicacao(Toplevel):
    Toplevel.destroy()      
    Toplevel.quit()
    root.destroy()
    os._exit(1) 
    
def fecharJanelaTopLevel(Toplevel):
    Toplevel.destroy()

def janelaNomeRepetido():
    newAlertWindow = Toplevel(root)
    newAlertWindow.title("Alerta!")
    newAlertWindow.geometry("300x100")
    newAlertWindow.configure(bg='#FFFF00')
    
    labelText = Label(newAlertWindow, text="Já existe um conteiner com esse nome!", width=40, height=2, bg="#FFF00F").grid(row=0)
    labelText = Label(newAlertWindow, text="Por favor escolha outro.", width=40, height=2, bg="#FFF00F").grid(row=1)
    
    okButton = Button(newAlertWindow, text="OK",command=lambda:fecharJanelaTopLevel(newAlertWindow))
    okButton.grid(row=3)

def janelaConteinerNaoVazio():
    newAlertWindow = Toplevel(root)
    newAlertWindow.title("Alerta!")
    newAlertWindow.geometry("300x100")
    newAlertWindow.configure(bg='#FFFF00')
    
    labelText = Label(newAlertWindow, text="O conteiner não esta vazio!", width=40, height=2, bg="#FFF00F").grid(row=0)
    okButton = Button(newAlertWindow, text="OK",command=lambda:fecharJanelaTopLevel(newAlertWindow))
    okButton.grid(row=1)

def janelaNomeVazio():
    newAlertWindow = Toplevel(root)
    newAlertWindow.title("Alerta!")
    newAlertWindow.geometry("300x100")
    newAlertWindow.configure(bg='#FFFF00')
    
    labelText = Label(newAlertWindow, text="O nome do conteiner está vazio!", width=40, height=2, bg="#FFF00F").grid(row=0)
    okButton = Button(newAlertWindow, text="OK",command=lambda:fecharJanelaTopLevel(newAlertWindow))
    okButton.grid(row=1)
    
def janelaConteinerPaiInexistente():
    newAlertWindow = Toplevel(root)
    newAlertWindow.title("Alerta!")
    newAlertWindow.geometry("300x100")
    newAlertWindow.configure(bg='#FFFF00')
    
    labelText = Label(newAlertWindow, text="O conteiner pai não existe!", width=40, height=2, bg="#FFF00F").grid(row=0)
    labelText = Label(newAlertWindow, text="Por favor informe um valido.", width=40, height=2, bg="#FFF00F").grid(row=1)
    okButton = Button(newAlertWindow, text="OK",command=lambda:fecharJanelaTopLevel(newAlertWindow))
    okButton.grid(row=2)

def janelaInicial():
    newWindow = Toplevel(root)
    newWindow.title("Espaço de Tuplas")
    newWindow.geometry("320x300")
    newWindow.configure(bg='#2288BB')

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecharAplicacao(newWindow))
    
    labelText = Label(newWindow, text="Gerenciador de Ambientes", width=45, height=5, bg="#FFF00F").grid(row=0)
    
    labelText = Label(newWindow, text="", width=33, bg='#2288BB').grid(row=1)
    
    confNuvemButton = Button(newWindow,text="Configurar Nuvem", width=40,command=lambda:janelaConfNuvem()).grid(row=2)    
    confHostButton = Button(newWindow,text="Configurar Host", width=40, command=lambda:janelaConfHost()).grid(row=3)  
    confVMButton = Button(newWindow,text="Configurar VM", width=40,command=lambda:janelaConfVM()).grid(row=4)    
    confProcessoButton = Button(newWindow,text="Configurar Processo",width=40, command=lambda:janelaConfProcesso()).grid(row=5)    
    
def clickCriarNuvem(ts, nomeNuvem, Toplevel):
    nuvens = listarNuvens(ts)
    
    if(nomeNuvem != ""):
        if (nomeNuvem in nuvens):
            janelaNomeRepetido()
        else:
            criarNuvem(ts, nomeNuvem)
            fecharJanelaTopLevel(Toplevel)
    else:
        janelaNomeVazio()
    
def clickExcluirNuvem(ts, nomeNuvem, Toplevel):
    if(nomeNuvem != ""):
        deletarNuvem(ts, nomeNuvem)
        fecharJanelaTopLevel(Toplevel)
    else:
        janelaNomeVazio()

def janelaConfNuvem():
    global lista_registro_processos 
    global tse
    newNuvemWindow = Toplevel(root)
    newNuvemWindow.title("ET: Configuração de Nuvem")
    newNuvemWindow.geometry("400x400")
    newNuvemWindow.configure(bg='#888888')
    newNuvemWindow.protocol("WM_DELETE_WINDOW", lambda:fecharJanelaTopLevel(newNuvemWindow))
    
    criarNuvemLabel = Label(newNuvemWindow, text="Configuração de Nuvem").grid(row=1)
    textArea = ScrolledText(newNuvemWindow, wrap = WORD, width = 40, height = 6.5, bg="#FFF", font = ("Callibri",9))
    textArea.grid(row=2)
    
    listagemNuvens(textArea)
    
    criarNuvemLabel = Label(newNuvemWindow, width = 60, text="", bg='#888888').grid(row=3)
    criarNuvemLabel = Label(newNuvemWindow, text="Cadastrar nova nuvem", bg='#FFF').grid(row=4)
    criarNuvemLabel = Label(newNuvemWindow, width = 60, text="", bg='#888888').grid(row=5)
    criarNuvemLabel = Label(newNuvemWindow, text="Nome da Nuvem", bg='#888888').grid(row=6)
    nuvemEntry = Entry(newNuvemWindow, width = 50)
    nuvemEntry.grid(row=7)
    criarNuvemButton = Button(newNuvemWindow,text="Criar Nuvem", width=30, command=lambda:clickCriarNuvem(tse, nuvemEntry.get(),newNuvemWindow))
    criarNuvemButton.grid(row=8)
    
    removerNuvemLabel = Label(newNuvemWindow, width = 60, text="", bg='#888888').grid(row=9)
    removerNuvemLabel = Label(newNuvemWindow, text="Excluir nuvem", bg='#FFF').grid(row=10)
    removerNuvemLabel = Label(newNuvemWindow, width = 60, text="", bg='#888888').grid(row=11)
    removerNuvemLabel = Label(newNuvemWindow, text="Nome da Nuvem", bg='#888888').grid(row=12)
    removerEntry = Entry(newNuvemWindow, width = 50)
    removerEntry.grid(row=13)
    removerNuvemButton = Button(newNuvemWindow,text="Excluir Nuvem", width=30, command=lambda:clickExcluirNuvem(tse, removerEntry.get(),newNuvemWindow))
    removerNuvemButton.grid(row=14)

def clickCriarHost(ts, nomeHost, nomeNuvem, Toplevel):
    hosts = listarHosts(ts)
    nuvens = listarNuvens(ts)
    
    if(nomeHost != "" and nomeNuvem!= ""):
        if (nomeNuvem in nuvens):
            if (nomeHost in hosts):
                janelaNomeRepetido()
            else:
                criarHost(ts, nomeHost)
                entrarNuvem(ts, nomeHost, nomeNuvem)
                fecharJanelaTopLevel(Toplevel)
        else:
            janelaConteinerPaiInexistente()
    else:
        janelaNomeVazio()
        
def clickCriarVM(ts, nomeVM, nomeHost, Toplevel):
    vms = listarVMs(ts)
    hosts = listarHosts(ts)
    
    if(nomeHost != "" and nomeVM!= ""):
        if (nomeVM in vms):
            if (nomeHost in hosts):
                janelaNomeRepetido()
            else:
                criarVM(ts, nomeVM)
                entrarHost(ts, nomeVM, nomeHost)
                fecharJanelaTopLevel(Toplevel)
        else:
            janelaConteinerPaiInexistente()
    else:
        janelaNomeVazio()
        
def clickCriarProcesso(ts, nomeProcesso, nomeVM, Toplevel):
    global lista_registro_processos
    global tse
    vms = listarVMs(ts)
    processos = listarProcessos(ts)
    
    if(nomeProcesso != "" and nomeVM!= ""):
        if (nomeVM in vms):
            if (nomeProcesso in processos):
                janelaNomeRepetido()
            else:
                criarProcesso(ts, nomeProcesso)
                entrarVM(ts, nomeProcesso, nomeVM)
                
                fecharJanelaTopLevel(Toplevel)
                
        else:
            janelaConteinerPaiInexistente()
    else:
        janelaNomeVazio()

def clickExcluirHost(ts, nomeHost, nomeNuvem, Toplevel):
    if(nomeNuvem != "" and nomeHost!= ""):
        deletarHost(ts, nomeNuvem)
        sairNuvem(ts, nomeHost, nomeNuvem)
        fecharJanelaTopLevel(Toplevel)
    else:
        janelaNomeVazio()

def clickExcluirVM(ts, nomeVM, nomeHost, Toplevel):
    if(nomeHost != "" and nomeVM!= ""):
        deletarVM(ts, nomeVM)
        sairHost(ts, nomeVM, nomeHost)
        fecharJanelaTopLevel(Toplevel)
    else:
        janelaNomeVazio()
        
def clickExcluirProcesso(ts, nomeProcesso, nomeVM, Toplevel):
    if(nomeVM != "" and nomeProcesso!= ""):
        deletarVM(ts, nomeProcesso)
        sairHost(ts, nomeProcesso, nomeVM)
        fecharJanelaTopLevel(Toplevel)
    else:
        janelaNomeVazio()

def janelaNuvemHosts(ts, nomeNuvem, tela):
    fecharJanelaTopLevel(tela)
    nuvemWindow = Toplevel(root)
    nuvemWindow.title("ET: Nuvem de Hosts")
    nuvemWindow.geometry("400x400")
    nuvemWindow.configure(bg='#274360')
    nuvemWindow.protocol("WM_DELETE_WINDOW", lambda:fecharJanelaTopLevel(nuvemWindow))
    
    hostLabel = Label(nuvemWindow, text="Hosts da Nuvem: "+nomeNuvem, width= 40).grid(row=1)
    
    textAreaHosts = ScrolledText(nuvemWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaHosts.grid(row=3)
    
    listagemHostsDaNuvem(textAreaHosts, nomeNuvem)
    
    removerHostLabel = Label(nuvemWindow, width = 60, text="", bg='#274360').grid(row=4)
    removerHostLabel = Label(nuvemWindow, text="Excluir Host", bg='#FFF').grid(row=5)
    removerHostLabel = Label(nuvemWindow, width = 60, text="", bg='#274360').grid(row=6)
    removerHostLabel = Label(nuvemWindow, text="Nome da Host", bg='#274360').grid(row=7)
    removerEntry = Entry(nuvemWindow, width = 50)
    removerEntry.grid(row=8)
    removerHostButton = Button(nuvemWindow,text="Excluir Host", width=30, command=lambda:clickExcluirHost(tse, removerEntry.get(), nomeNuvem, nuvemWindow))
    removerHostButton.grid(row=9)
    
def janelaHostVMs(ts, nomeHost, tela):
    fecharJanelaTopLevel(tela)
    hostWindow = Toplevel(root)
    hostWindow.title("ET: Host de VMs")
    hostWindow.geometry("400x400")
    hostWindow.configure(bg='#274360')
    hostWindow.protocol("WM_DELETE_WINDOW", lambda:fecharJanelaTopLevel(hostWindow))
    
    hostLabel = Label(hostWindow, text="VMs do Host: "+nomeHost, width= 40).grid(row=1)
    
    textAreaVMs = ScrolledText(hostWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaVMs.grid(row=3)
    
    listagemVMsDoHost(textAreaVMs, nomeHost)
    
    removerVMLabel = Label(hostWindow, width = 60, text="", bg='#274360').grid(row=4)
    removerVMLabel = Label(hostWindow, text="Excluir VM", bg='#FFF').grid(row=5)
    removerVMLabel = Label(hostWindow, width = 60, text="", bg='#274360').grid(row=6)
    removerVMLabel = Label(hostWindow, text="Nome da VM", bg='#274360').grid(row=7)
    removerEntry = Entry(hostWindow, width = 50)
    removerEntry.grid(row=8)
    removerVMButton = Button(hostWindow,text="Excluir VM", width=30, command=lambda:clickExcluirVM(tse, removerEntry.get(), nomeHost, hostWindow))
    removerVMButton.grid(row=9)
    
def janelaVmProcessos(ts, nomeVM, tela):
    fecharJanelaTopLevel(tela)
    vmWindow = Toplevel(root)
    vmWindow.title("ET: VMs de Processos")
    vmWindow.geometry("400x400")
    vmWindow.configure(bg='#274360')
    vmWindow.protocol("WM_DELETE_WINDOW", lambda:fecharJanelaTopLevel(vmWindow))
    
    vmLabel = Label(vmWindow, text="Processos do VM: "+nomeVM, width= 40).grid(row=1)
    
    textAreaProcessos = ScrolledText(vmWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaProcessos.grid(row=3)
    
    listagemProcessosDaVM(textAreaProcessos, nomeVM)
    
    removerVMLabel = Label(vmWindow, width = 60, text="", bg='#274360').grid(row=4)
    removerVMLabel = Label(vmWindow, text="Excluir VM", bg='#FFF').grid(row=5)
    removerVMLabel = Label(vmWindow, width = 60, text="", bg='#274360').grid(row=6)
    removerVMLabel = Label(vmWindow, text="Nome da VM", bg='#274360').grid(row=7)
    removerEntry = Entry(vmWindow, width = 50)
    removerEntry.grid(row=8)
    removerVMButton = Button(vmWindow,text="Excluir VM", width=30, command=lambda:clickExcluirProcesso(tse, removerEntry.get(), nomeVM, vmWindow))
    removerVMButton.grid(row=9)
    
    acessarProcessoLabel = Label(vmWindow, width = 60, text="", bg='#274360').grid(row=10)
    acessarProcessoLabel = Label(vmWindow, text="Exibir Processo", bg='#FFF').grid(row=11)
    acessarProcessoLabel = Label(vmWindow, width = 60, text="", bg='#274360').grid(row=12)
    acessarProcessoLabel = Label(vmWindow, text="Nome do Processo", bg='#274360').grid(row=13)
    acessarProcessoEntry = Entry(vmWindow, width = 50)
    acessarProcessoEntry.grid(row=14)
    acessarProcessoButton = Button(vmWindow,text="Abrir Processo", width=30, command=lambda:janelaProcesso(acessarProcessoEntry.get(), nomeVM))
    acessarProcessoButton.grid(row=15)
    
                
def janelaConfHost():
    newHostWindow = Toplevel(root)
    newHostWindow.title("ET: Configuração de Host")
    newHostWindow.geometry("400x400")
    newHostWindow.configure(bg='#888888')
    newHostWindow.protocol("WM_DELETE_WINDOW", lambda:fecharJanelaTopLevel(newHostWindow))
    
    criarHostLabel = Label(newHostWindow, text="Configuração de Host").grid(row=1)
    textAreaNuvens = ScrolledText(newHostWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaNuvens.grid(row=3)
    
    listagemNuvens(textAreaNuvens)
    
    textAreaHosts = ScrolledText(newHostWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaHosts.grid(row=4)
    listagemHosts(textAreaHosts)
    
    criarHostLabel = Label(newHostWindow, width = 60, text="", bg='#888888').grid(row=5)
    criarHostLabel = Label(newHostWindow, text="Cadastrar novo host", bg='#FFF').grid(row=6)
    criarHostLabel = Label(newHostWindow, width = 60, text="", bg='#888888').grid(row=7)
    criarHostLabel = Label(newHostWindow, text="Nome do Host", bg='#888888').grid(row=8)
    hostEntry = Entry(newHostWindow, width = 50)
    hostEntry.grid(row=9)
    criarHostLabel = Label(newHostWindow, text="Informe a Nuvem em que deseja adicionar o Host", bg='#888888').grid(row=10)
    hostEntryNuvem = Entry(newHostWindow, width = 50)
    hostEntryNuvem.grid(row=11)
    
    criarHostButton = Button(newHostWindow,text="Criar Host", width=30, command=lambda:clickCriarHost(tse, hostEntry.get(), hostEntryNuvem.get(),newHostWindow))
    criarHostButton.grid(row=12)
    
    criarHostLabel = Label(newHostWindow, width = 60, text="", bg='#888888').grid(row=13)
    criarHostLabel = Label(newHostWindow, text="Verificar Hosts por Nuvem", bg='#FFF').grid(row=14)
    criarHostLabel = Label(newHostWindow, text="Informe o nome da Nuvem", bg='#888888').grid(row=15)
    hostVerEntry = Entry(newHostWindow, width = 50)
    hostVerEntry.grid(row=16)
    
    verHostButton = Button(newHostWindow,text="Ver Hosts", width=30, command=lambda:janelaNuvemHosts(tse, hostVerEntry.get(), newHostWindow))
    verHostButton.grid(row=17)

def clickCriarVM(ts, nomeVM, nomeHost, Toplevel):
    hosts = listarHosts(ts)
    vms = listarVMs(ts)
    
    if(nomeVM != "" and nomeHost!= ""):
        if (nomeHost in hosts):
            if (nomeVM in vms):
                janelaNomeRepetido()
            else:
                criarVM(ts, nomeVM)
                entrarHost(ts, nomeVM, nomeHost)
                fecharJanelaTopLevel(Toplevel)
        else:
            janelaConteinerPaiInexistente()
    else:
        janelaNomeVazio()
    
def janelaConfVM():
    newVMWindow = Toplevel(root)
    newVMWindow.title("ET: Configuração de VM")
    newVMWindow.geometry("400x400")
    newVMWindow.configure(bg='#888888')
    newVMWindow.protocol("WM_DELETE_WINDOW", lambda:fecharJanelaTopLevel(newVMWindow))
    
    criarVMLabel = Label(newVMWindow, text="Configuração de VM").grid(row=1)
    textAreaHosts = ScrolledText(newVMWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaHosts.grid(row=3)
    
    listagemHosts(textAreaHosts)
    
    textAreaVMs = ScrolledText(newVMWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaVMs.grid(row=4)
    listagemVMs(textAreaVMs)
    
    criarVMLabel = Label(newVMWindow, width = 60, text="", bg='#888888').grid(row=5)
    criarVMLabel = Label(newVMWindow, text="Cadastrar novo host", bg='#FFF').grid(row=6)
    criarVMLabel = Label(newVMWindow, width = 60, text="", bg='#888888').grid(row=7)
    criarVMLabel = Label(newVMWindow, text="Nome do VM", bg='#888888').grid(row=8)
    hostEntry = Entry(newVMWindow, width = 50)
    hostEntry.grid(row=9)
    criarVMLabel = Label(newVMWindow, text="Informe a Host em que deseja adicionar o VM", bg='#888888').grid(row=10)
    hostEntryHost = Entry(newVMWindow, width = 50)
    hostEntryHost.grid(row=11)
    
    criarVMButton = Button(newVMWindow,text="Criar VM", width=30, command=lambda:clickCriarVM(tse, hostEntry.get(), hostEntryHost.get(),newVMWindow))
    criarVMButton.grid(row=12)
    
    criarVMLabel = Label(newVMWindow, width = 60, text="", bg='#888888').grid(row=13)
    criarVMLabel = Label(newVMWindow, text="Verificar VMs por Host", bg='#FFF').grid(row=14)
    criarVMLabel = Label(newVMWindow, text="Informe o nome da Host", bg='#888888').grid(row=15)
    hostVerEntry = Entry(newVMWindow, width = 50)
    hostVerEntry.grid(row=16)
    
    verVMButton = Button(newVMWindow,text="Ver VMs", width=30, command=lambda:janelaHostVMs(tse, hostVerEntry.get(), newVMWindow))
    verVMButton.grid(row=17)

def clickCriarProcesso(ts, nomeProcesso, nomeVM, Toplevel):
    processos = listarProcessos(ts)
    vms = listarVMs(ts)
    
    if(nomeVM != "" and nomeProcesso!= ""):
        if (nomeVM in vms):
            if (nomeProcesso in processos):
                janelaNomeRepetido()
            else:
                criarProcesso(ts, nomeProcesso)
                entrarVM(ts, nomeProcesso, nomeVM)
                fecharJanelaTopLevel(Toplevel)
        else:
            janelaConteinerPaiInexistente()
    else:
        janelaNomeVazio()

def janelaConfProcesso():
    newProcessoWindow = Toplevel(root)
    newProcessoWindow.title("ET: Configuração de Processo")
    newProcessoWindow.geometry("400x400")
    newProcessoWindow.configure(bg='#888888')
    newProcessoWindow.protocol("WM_DELETE_WINDOW", lambda:fecharJanelaTopLevel(newProcessoWindow))
    
    criarProcessoLabel = Label(newProcessoWindow, text="Configuração de Processo").grid(row=1)
    textAreaHosts = ScrolledText(newProcessoWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaHosts.grid(row=3)
    
    listagemVMs(textAreaHosts)
    
    textAreaProcessos = ScrolledText(newProcessoWindow, wrap = WORD, width = 40, height = 3, bg="#FFF", font = ("Callibri",9))
    textAreaProcessos.grid(row=4)
    listagemProcessos(textAreaProcessos)
    
    criarProcessoLabel = Label(newProcessoWindow, width = 60, text="", bg='#888888').grid(row=5)
    criarProcessoLabel = Label(newProcessoWindow, text="Cadastrar nova vm", bg='#FFF').grid(row=6)
    criarProcessoLabel = Label(newProcessoWindow, width = 60, text="", bg='#888888').grid(row=7)
    criarProcessoLabel = Label(newProcessoWindow, text="Nome do Processo", bg='#888888').grid(row=8)
    vmEntry = Entry(newProcessoWindow, width = 50)
    vmEntry.grid(row=9)
    criarProcessoLabel = Label(newProcessoWindow, text="Informe a VM em que deseja adicionar o Processo", bg='#888888').grid(row=10)
    vmEntryHost = Entry(newProcessoWindow, width = 50)
    vmEntryHost.grid(row=11)
    
    criarProcessoButton = Button(newProcessoWindow,text="Criar Processo", width=30, command=lambda:clickCriarProcesso(tse, vmEntry.get(), vmEntryHost.get(),newProcessoWindow))
    criarProcessoButton.grid(row=12)
    
    criarProcessoLabel = Label(newProcessoWindow, width = 60, text="", bg='#888888').grid(row=13)
    criarProcessoLabel = Label(newProcessoWindow, text="Verificar Processos por VM", bg='#FFF').grid(row=14)
    criarProcessoLabel = Label(newProcessoWindow, text="Informe o nome da VM", bg='#888888').grid(row=15)
    vmVerEntry = Entry(newProcessoWindow, width = 50)
    vmVerEntry.grid(row=16)
    
    verProcessoButton = Button(newProcessoWindow,text="Ver Processo", width=30, command=lambda:janelaVmProcessos(tse, vmVerEntry.get(), newProcessoWindow))
    verProcessoButton.grid(row=17)

# Envia a mensagem do usuário para as outras Tuplas de usuários na sala                                  
def envia_mensagem(entry_widget,nomeProcesso,vmAtual,destinatario):
    global tse 
    global lista_registro_processos
    msg = entry_widget
    
    if(msg != ""):
        mandarMensagem(tse, vmAtual, nomeProcesso, destinatario, msg)
        for i in range(len(lista_registro_processos)): 
            lista_registro_processos[i][1] = 1 # <-- 'Setamos' a flag de todos os usuários na lista que armazena seus nomes e suas flags para o valor de '1'!

# Envia a mensagem do usuário para as outras Tuplas de usuários na sala ('Loop' que checa por novas mensagens enviadas)
def recebe_mensagens(newWindowInput,ScrolledText,nomeProcesso,vmAtual):
    global tse
    global lista_registro_processos    
    msg_recebida = recebeMensagem(tse, vmAtual)
    
    
    for i in lista_registro_processos:
        if i[0] == nomeProcesso:
            if i[1] == 1: # <--  verifica se o usuário em específico está com sua flag como '1', se tiver, o usuário atualizará as msgs do seu chat pois há novas msgs!
                if(msg_recebida[0][0] == nomeProcesso):
                    ScrolledText.insert(tk.INSERT,"Nova mensagem:\n")
                    ScrolledText.insert(tk.INSERT,msg_recebida[0][1]+"\n", 'msg')
                    i[1] = 0
            else:
                pass   

    newWindowInput.after(1,lambda:recebe_mensagens(newWindowInput,ScrolledText,nomeProcesso,vmAtual))

    
def janelaProcesso(processo, vm):
    global lista_registro_processos
    global tse
    
    processoWindow = Toplevel(root)
    processoWindow.title("ET: Processo: "+processo)
    processoWindow.geometry("400x400")
    processoWindow.configure(bg='#888888')
    processoWindow.protocol("WM_DELETE_WINDOW", lambda:fecharJanelaTopLevel(processoWindow))
    
    criarProcessoLabel = Label(processoWindow, text="Mensagens Recebidas").grid(row=1)
    textAreaProcessos = ScrolledText(processoWindow, wrap = WORD, width = 40, height = 5, bg="#0F0", font = ("Callibri",9))
    textAreaProcessos.grid(row=3)
    
    textAreaProcessos.insert(tk.INSERT, "Mensagens recebidas...\n")
    
    criarProcessoLabel = Label(processoWindow, text="Enviar Mensagem").grid(row=4)
    criarProcessoLabel = Label(processoWindow, text="Destinatario").grid(row=5)
    destinatarioEntry = Entry(processoWindow, width = 50)
    destinatarioEntry.grid(row=6)
    
    criarProcessoLabel = Label(processoWindow, text="Mensagem").grid(row=7)
    mensagemEntry = Entry(processoWindow, width = 50)
    mensagemEntry.grid(row=8)
    
    verProcessoButton = Button(processoWindow,text="Enviar Mensagem", width=30, command=lambda:envia_mensagem(mensagemEntry.get(), processo, vm, destinatarioEntry.get()))
    verProcessoButton.grid(row=9)
    
    processoWindow.after(1,lambda:recebe_mensagens(processoWindow, textAreaProcessos, processo, vm))
    
def listagemNuvens(ScrolledText):
    global lista_registro_processos
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: Nuvens Disponiveis: ...\n")
    lista = listarNuvens(tse)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")


def listagemHosts(ScrolledText):
    global lista_registro_processos
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: Hosts Disponiveis: ...\n")
    lista = listarHosts(tse)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")


def listagemVMs(ScrolledText):
    global lista_registro_processos
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: VMs Disponiveis: ...\n")
    lista = listarVMs(tse)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")


def listagemProcessos(ScrolledText):
    global lista_registro_processos
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: Processos Disponiveis: ...\n")
    lista = listarProcessos(tse)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")


def listagemHostsDaNuvem(ScrolledText, nomeNuvem):
    global lista_registro_processos
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: Hosts na Nuvem: ...\n")
    lista = listarIntegrantesNuvem(tse, nomeNuvem)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")


def listagemVMsDoHost(ScrolledText, nomeHost):
    global lista_registro_processos
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: VMs no Host: ...\n")
    lista = listarIntegrantesHost(tse, nomeHost)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")

    
def listagemProcessosDaVM(ScrolledText, nomeVM):
    global lista_registro_processos
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: Processos na VM: ...\n")
    lista = listarIntegrantesVM(tse, nomeVM)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")


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

    janelaInicial()
    root.mainloop()