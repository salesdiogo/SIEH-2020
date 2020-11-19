
#coding=utf-8

#msg = "Hello World"
#print(str.upper(msg))


ip_subnet_mask_C = "192.168.1." 

ips = [] 

ips = [ip_subnet_mask_C + str(ip) for ip in range(255)]

print(ips)