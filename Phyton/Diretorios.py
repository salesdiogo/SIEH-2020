#coding=utf-8
import os 
import platform

SO=platform.system()
print(SO+" é o sistema operacional utilizado")

print("Para criar diretorio digite 1")
print("Para renomear diretorio digite 1")
print("Para remover diretorio digite 1")
print("Para listar diretorio digite 1")

numero= input("Digite o numero para a ação: " )

def listDir():
    if SO=="Linux":
        listCMD='ls -la'
    
    elif SO=="Windows":
        listCMD='dir'

    os.system(listCMD)   


if int(numero) == 1:
    print("Diretorio sera criado em "+ os.getcwd()+" ...")
    diretorio=input(" Insira o nome da diretorio/pasta:")
    os.mkdir(diretorio)


elif int(numero) == 2:
    print("Diretorio sera renomeado em "+ os.getcwd()+" ...")
    diretorio=input(" Insira o nome da diretorio/pasta:")
    os.rename(diretorio,'nome_alterado')

elif int(numero) == 3:
    print("Diretorio sera renomeado em "+ os.getcwd()+" ...")
    diretorio=input(" Insira o nome da diretorio/pasta:")
    os.rmdir(diretorio)

elif int(numero) == 4:
    print("Diretorio sera listado em "+ os.getcwd()+" ...")
    listDir()

else: 
    print("Digite um numero entre 1 e 4")