#coding=utf-8

#Lista de IPs

lista_IP = []
range_IP = "192.168.1."
file = open("ipList.txt","w")
[file.write(range_IP + str(ip) + "\n") for ip in range(1,256)]
file.close


#Lista de Numeros

lista_NUM = []
file = open ("portList.txt","w")
[file.write(str(numero) + "\n") for numero in range(1, 1025)]
file.close()

