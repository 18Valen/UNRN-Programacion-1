archivo = open("temperaturas.txt", "r")

temperaturas = []

for linea in archivo:
    linea = linea.strip().split(";")
    temperaturas.append(linea)

temperaturas_dic = {}
for temperatura in temperaturas:
    if not temperatura[0] in temperaturas_dic:
        temperaturas_dic[temperatura[0]] = [temperatura[1]]
    else:
        temperaturas_dic[temperatura[0]].append(temperatura[1])

print(temperaturas_dic)
