#coding=utf-8
import socket
import sys

from datetime import datetime

ficheiro_scanner=open('resultados.txt', 'w')
open_ports=[]


inicio=datetime.now()


def portscan(ip,port):


    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=sock.connect_ex((ip,port))
    if result==0:
        print("Port {}:     Open".format(port))
        open_ports.append(str(port))
    
    
    ficheiro_scanner.writelines(open_ports)
    
    sock.close()

ip=input("Digite o IP: ")


try:
    for i in range(1024):
        portscan(ip,i)


except KeyboardInterrupt:
    print("Scanner interrompido com ctrl+c")
    sys.exit()

except socket.gaierror:
    print("host não encontrado")
    sys.exit()

except socket.error:
    print("Houve um erro de conexão")
    sys.exit()

 
ficheiro_scanner.close() 

fim=datetime.now()

total=fim-inicio

print("tempo total de scan " +str(total))