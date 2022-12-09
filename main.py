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
    
    verHostButton = Button(newHostWindow,text="Ver Host", width=30, command=lambda:print(hostVerEntry.get()))
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
    
    verVMButton = Button(newVMWindow,text="Ver VM", width=30, command=lambda:print(hostVerEntry.get()))
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
    criarProcessoLabel = Label(newProcessoWindow, text="Informe a Host em que deseja adicionar o Processo", bg='#888888').grid(row=10)
    vmEntryHost = Entry(newProcessoWindow, width = 50)
    vmEntryHost.grid(row=11)
    
    criarProcessoButton = Button(newProcessoWindow,text="Criar Processo", width=30, command=lambda:clickCriarProcesso(tse, vmEntry.get(), vmEntryHost.get(),newProcessoWindow))
    criarProcessoButton.grid(row=12)
    
    criarProcessoLabel = Label(newProcessoWindow, width = 60, text="", bg='#888888').grid(row=13)
    criarProcessoLabel = Label(newProcessoWindow, text="Verificar Processos por Host", bg='#FFF').grid(row=14)
    criarProcessoLabel = Label(newProcessoWindow, text="Informe o nome da Host", bg='#888888').grid(row=15)
    vmVerEntry = Entry(newProcessoWindow, width = 50)
    vmVerEntry.grid(row=16)
    
    verProcessoButton = Button(newProcessoWindow,text="Ver Processo", width=30, command=lambda:print(vmVerEntry.get()))
    verProcessoButton.grid(row=17)

def listagemNuvens(ScrolledText):
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: Nuvens Disponiveis: ...\n")
    lista = listarNuvens(tse)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")
    print(*lista, sep='\n')

def listagemHosts(ScrolledText):
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: HOSTS Disponiveis: ...\n")
    lista = listarHosts(tse)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")
    print(*lista, sep='\n')
    ScrolledText.insert(tk.INSERT,"\n\n ...\n") 

def listagemVMs(ScrolledText):
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: VMS: ...\n")
    lista = listarVMs(tse)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")
    print(*lista, sep='\n')
    ScrolledText.insert(tk.INSERT,"\n\n ...\n") 

def listagemProcessos(ScrolledText):
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: PROCESSOS: ...\n")
    lista = listarProcessos(tse)
    ScrolledText.insert(tk.INSERT,str(lista)+"\n")
    print(*lista, sep='\n')
    ScrolledText.insert(tk.INSERT,"\n\n ...\n") 


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