baralho = []
with open("cartas.txt", "r", encoding = "UTF-8") as arquivo:
	for linha in arquivo:
		baralho.append(linha[:-1].split(';'))
	baralho.pop(0)

print(baralho)
print(len(baralho))
input()