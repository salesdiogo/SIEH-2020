
#coding=utf-8

SistemasOperacionais = ["windows","macos","linux","solaris","android","ios"]

#Loop 1
ficheiro = "loop1.txt"
file = open(ficheiro,"w") 
for x in SistemasOperacionais:
        if x != "solaris":
            print(x)
            file.write(x+ "\n") 
file.close()

#Loop2
ficheiro2 = "loop2.txt"

file = open(ficheiro2, "w")

a = 0
while a < len(SistemasOperacionais):
	b = SistemasOperacionais[a]
	if b != "solaris":
		print(b)
		file.write(b + "\n")
	a += 1

file.close()
