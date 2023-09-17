def lercartas(): #bloco responsavel por ler oarquivo e transformar em matriz
	baralho = []
	with open("cartas.txt", "r", encoding = "UTF-8") as arquivo:
		for linha in arquivo:
			baralho.append(linha[:-1].split(';')) # O linha[:-1] esta garantindo que so vai apendar a linha do arquivo ate antes da quebra de linha
		baralho.pop(0) #Eliminando o primeiro item da matriz pois não é uma carta
		return baralho


def ordenar(escolha,deck): #função responsavel pela ordenação, o que ela faz é receber o modo de jogo escolhido e a mão dos jogadores e ordenar de acordo com a escolha durante o jogo
	aux =  0
	cartas = deck
	modo = escolha
	if escolha >= 0 and escolha <= 3:
		for i in range(0,4):
			for j in range(0,4):
				if cartas[i][modo] < cartas[j][modo]: #veerifica caratas duas a duas se de acordo com o modo de jogo uma é menor que a outra
					aux = cartas[i] # a vaariavel auxiliar(aux) é responsavel por guardar um valor para ele n ser perdido durante a troca de posições
					cartas[i] = cartas[j]
					cartas[j] = aux
	return cartas

def embaralha(carta): #função responsavel por embaralar o deck
	from random import randint
	crupie = carta
	b = 0
	for i in range(0,len(crupie)-1):
		x = randint(0,len(crupie)-1) # sorteando um numero aleatorio
		for j in range(0,4):
			if crupie[x][j] != crupie[j][j]: #comparando valores
				b = crupie[j] #variavel auxiliar recebendo carta para não perde-la
				crupie[j] = crupie[x] #pegando uma carta e substituindo por outra aleatoria
				crupie[x] = b
	return crupie



def distribui(m): #função responsavel por diistribuir as cartas ao jogador
	c = m
	hand = []
	for i in range (0,5):
		hand.append(c.pop()) #Esta tirando as cartas da matriz como se fosse um baralho simulando uma pilha e colocando na mão dos jogadores
	return hand

def descarte(z,c,b): #função de desarte recebendo três valores:
	d = z # A mão do jogador
	carta = c # A carta a ser descartada
	monte = b # O baralho
	descarte = []
	descarte.append(carta) #colocando carta descartada na area de descarte
	d.pop(carta) #Tirando carta da mão do jogador
	d.append(monte.pop()) #Pegando a carta do topo do deck e clocando na mão do jogador


class nicks: #classe para armazenar os jogadores
	def _init_(self):
		self.nome = ""
		self.score = 0.0

def cadastro(pontos): #Cadastro dos jogadores
	a = nicks() #variavel recebendo a classe
	dicionarioJ = {}
	print("Entre com o nick")
	a.nome = input("Digite o nick: ")
	a.score = pontos
	dicionarioJ[a.nome] = a.score #colocando jogador dentro de um dicionario que tem como chave e valor objetos da classe

	return dicionarioJ

def binario(dicionarioJ,ler): #Banco de dados
        import pickle #biblioteca binaria
        l = ler
        dados  = dicionarioJ
        if l == 0: #codinção que diz que se o jogador quer salvar seu score
                with open("score.dat", "ab") as arquivoR:
                        pickle.dump(dados,arquivoR)
        elif l == 1: #condição para ler os scores ja salvo 
                with open("score.dat", "rb") as arquivoL:
                        data = pickle.load(arquivoL)

                        return data


#Bloco responsavel pelo JOKENPO
def jokenpo(jogador1,jogador2,pontosj1,pontosj2,maoj1,maoj2):
	if jogador1[len(maoj1)-1][4] == "Pedra" and jogador2[len(maoj2)-1][4] == "Pedra":
		print("Empate")
		descarte(maoj1,len(maoj1)-1,embaralha(lercartas()))
		descarte(maoj2,len(maoj2)-1,embaralha(lercartas()))
	elif jogador1[len(maoj1)-1][4] == "Pedra" and jogador2[len(maoj2)-1][4] == "Papel":
		print("Vencedor: Jogador 2")
		pontosj2+=1
		descarte(maoj1,len(maoj1)-1,embaralha(lercartas()))
		maoj2.pop(len(maoj2)-1)
	elif jogador1[len(maoj1)-1][4] == "Pedra" and jogador2[len(maoj2)-1][4] == "Tesouta":
		print("Vencedor: Jogador 1")
		pontosj1+=1
		descarte(maoj2,len(maoj2)-1,embaralha(lercartas()))
		maoj1.pop(len(maoj1)-1)
	elif jogador1[len(maoj1)-1][4] == "Papel" and jogador2[len(maoj2)-1][4] == "Pedra":
		print("Vencedor: Jogador 1")
		pontosj1+=1
		descarte(maoj2,len(maoj2)-1,embaralha(lercartas()))
		maoj1.pop(len(maoj1)-1)
	elif jogador1[len(maoj1)-1][4] == "Papel" and jogador2[len(maoj2)-1][4] == "Tesouta":
		print("Vencedor: Jogador 2")
		pontosj2+=1
		descarte(maoj1,len(maoj1)-1,embaralha(lercartas()))
		maoj2.pop(len(maoj2)-1)
	elif jogador1[len(maoj1)-1][4] == "Papel" and jogador2[len(maoj2)-1][4] == "Papel":
		print("Empate")
		descarte(maoj1,len(maoj1)-1,embaralha(lercartas()))
		descarte(maoj2,len(maoj2)-1,embaralha(lercartas()))
	elif jogador1[len(maoj1)-1][4] == "Tesoura" and jogador2[len(maoj2)-1][4] == "Tesouta":
		print("Empate")
		descarte(maoj1,len(maoj1)-1,embaralha(lercartas()))
		descarte(maoj2,len(maoj2)-1,embaralha(lercartas()))
	elif jogador1[len(maoj1)-1][4] == "Tesoura" and jogador2[len(maoj2)-1][4] == "Papel":
		print("Vencedor: Jogador 1")
		pontosj1+=1
		descarte(maoj2,len(maoj2)-1,embaralha(lercartas()))
		maoj1.pop(len(maoj1)-1)
	elif jogador1[len(maoj1)-1][4] == "Tesoura" and jogador2[len(maoj2)-1][4] == "Pedra":
		print("Vencedor: Jogador 1")
		pontosj2+=1
		descarte(maoj1,len(maoj1)-1,embaralha(lercartas()))
		maoj2.pop(len(maoj2)-1)
#Bloco do jogo 
def game():
	pontosj1 = 0 #Pontos do jogador 1 
	pontosj2 = 0 #Pontos do jogador 2
	rodadas = 0
	print("Bem vindos")
	print("/////////////////////////////////////////////////////////////////////////")
	print("Scores anteriores: {}".format( binario(0,1))) #Exibindo dados de jogadores anteriores
	print("/////////////////////////////////////////////////////////////////////////")
	print("Escolham o modo de jogo")
	print("Digite 1 para modo ALEATORIO e 2 para o modo Manual: ")
	jogo = int(input("Escolha: "))
	while rodadas <= 5: #Dentro do laço é onde todas as regras do jogo serão aplicadas. Para mais informações leia o relatorio
		if jogo == 1:
                        #chamando funções do deck e de embaralhar
			deckpronto = embaralha(lercartas())
			#distribuindo cartas
			maoj1 = distribui(deckpronto)
			maoj2 = distribui(deckpronto)
			print("/////////////////////////////////////////////////////////////////////////")
			print("Vez do jogador1")
			print(maoj1)
			escolha=int(input("Digite 1 para disputar com o atributo valor 2 para disputar com o atributo força 3 para disputar com o atributo energia e 4 para disputar com jokenpo: "))
			if escolha >= 1 and escolha <=3:
				mj1 = ordenar(escolha,maoj1)
				mj2 = ordenar(escolha,maoj2)
				print(mj1)
				terminar = int(input("Digite 0 se ja viu suas cartas e vire a tela para o outro jogador: "))
				print(mj2)
				if mj1[len(mj1) -1][escolha] > mj2[len(mj2)-1][escolha]:
					print("Vencedor: Jogador1")
					pontosj1+=1
					descarte(mj2,len(mj2)-1,embaralha(lercartas()))
					maoj1.pop(len(mj1)-1)
				elif  mj1[len(mj1)-1][escolha] == mj2[len(mj2)-1][escolha]:
					print("Empate")
					descarte(mj1,len(mj1)-1,embaralha(lercartas()))
					descarte(mj2,len(mj2)-1,embaralha(lercartas()))
				else:
					print("Vencedor: Jogador2")
					pontosj2+=1
					descarte(mj1,len(mj1)-1,embaralha(lercartas()))
					maoj2.pop(len(mj2)-1)
			elif escolha == 4:
				jokenpo(maoj1,maoj2,pontosj1,pontosj2,maoj1,maoj2)
			rodadas+=1
			if len(mj1) == 0 or len(mj2) == 0:
				break
			print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
			print("Vez do jogador2")
			if escolha >=1 and escolha <=3:	
				maoj1 = distribui(deckpronto)
				maoj2 = distribui(deckpronto)
				print(maoj2)
				escolha=int(input("Digite 1 para disputar com o atributo valor 2 para disputar com o atributo força 3 para disputar com o atributo energia e 4 para disputar com jokenpo: "))
				mj1 = ordenar(escolha,maoj1)
				mj2 = ordenar(escolha,maoj2)
				print(mj2)
				terminar = int(input("Digite 0 se ja viu suas cartas e vire a tela para o outro jogador: "))
				print(mj1)
				if mj1[len(mj1)-1][escolha] > mj2[len(mj2)-1][escolha]:
					print("Vencedor: Jogador 1")
					pontosj1+=1
					descarte(mj2,len(mj2)-1,embaralha(lercartas()))
					maoj1.pop(len(maoj1)-1)
				elif  mj1[len(mj1)-1][escolha] == mj2[len(mj2)-1][escolha]:
					print("Empate")
					descarte(mj1,len(mj1)-1,embaralha(lercartas()))
					descarte(mj2,len(mj2)-1,embaralha(lercartas()))
				else:
					print("Vencedor: Jogador 2")
					pontosj2+=1
					descarte(mj1,len(mj1)-1,embaralha(lercartas()))
					maoj2.pop(len(mj2)-1)
			elif escolha == 4:
				jokenpo(maoj1,maoj2,pontosj1,pontosj2,maoj1,maoj2)
			if len(mj1) == 0 or len(mj2) == 0:
				break
			rodadas+=1
		elif jogo == 2:
			deckpronto = embaralha(lercartas())
			maoj1 = distribui(deckpronto)
			maoj2 = distribui(deckpronto)
			mj1 = ordenar(0,maoj1)
			mj2 = ordenar(0,maoj2)
			print("Vez do jogador1")
			print(maoj1)
			escolha=int(input("Digite 1 para disputar com o atributo valor 2 para disputar com o atributo força 3 para disputar com o atributo energia e 4 para disputar com jokenpo: "))
			carta1 = int(input("Escolha a carta(a contagem das cartas é feita a partir do 0): "))
			print(mj1)
			terminar = int(input("Digite 0 se ja viu suas cartas e vire a tela para o outro jogador: "))
			if escolha == 1:
				print("Atributo escolhido: VALOR")
			elif escolha == 2:
				print("Atributo escolhido: FORÇA")
			elif escolha == 3:
				print("Atributo escolhido: ENERGIA")
			else:
				print("Atributo escolhido jokenpo")
			print(mj2)
			carta2 = int(input("Escolha a carta(a contagem das cartas é feita a partir do 0): "))
			if escolha >= 1 and escolha <=3:
				if mj1[carta1][escolha] > mj2[carta2][escolha]:
					print("Vencedor: Jogador 1")
					pontosj1+=1
					descarte(mj2,carta2,embaralha(lercartas()))
					mj1.pop(carta1)
				elif  mj1[carta1][escolha] == mj2[carta2][escolha]:
					print("Empate")
					descarte(mj1,carta1,embaralha(lercartas()))
					descarte(mj2,carta2,embaralha(lercartas()))
				else:
					print("Vencedor: Jogador 2")
					pontosj2+=1
					descarte(mj1,carta1,embaralha(lercartas()))
					mj2.pop(carta2)
			elif escolha == 4:
				jokenpo(maoj1,maoj2,pontosj1,pontosj2,maoj1,maoj2)
			if len(mj1) == 0 or len(mj2) == 0:
				break
			rodadas+=1
			print("Vez do jogador2")
			mj1 = ordenar(0,maoj1)
			mj2 = ordenar(0,maoj2)
			print(maoj2)
			escolha=int(input("Digite 1 para disputar com o atributo valor 2 para disputar com o atributo força 3 para disputar com o atributo energia e 4 para disputar com jokenpo:"))
			carta2 = int(input("Escolha a carta(a contagem das cartas é feita a partir do 0): "))
			print(mj2)
			terminar = int(input("Digite 0 se ja viu suas cartas e vire a tela para o outro jogador: "))
			if escolha == 1:
				print("Atributo escolhido: VALOR")
			elif escolha == 2:
				print("Atributo escolhido: FORÇA")
			elif escolha == 3:
				print("Atributo escolhido: ENERGIA")
			else:
				print("Atributo escolhido jokenpo")
			print(mj1)
			carta1 = int(input("Escolha a carta(a contagem das cartas é feita a partir do 0): "))
			if escolha >= 1 and escolha <=3:
				if mj1[carta1][escolha] > mj2[carta2][escolha]:
					print("Vencedor: Jogador 1")
					pontosj1+=1
					descarte(mj2,carta2,embaralha(lercartas()))
					mj1.pop(carta1)
				elif  mj1[carta1][escolha] == mj2[carta2][escolha]:
					print("Empate")
					descarte(mj1,carta1,embaralha(lercartas()))
					descarte(mj2,carta2,embaralha(lercartas()))
				else:
					print("Vencedor: Jogador 2")
					pontosj2+=1
					descarte(mj1,carta1,embaralha(lercartas()))
					mj2.pop(carta2)
			elif escolha == 4:
				jokenpo(maoj1,maoj2,pontosj1,pontosj2,maoj1,maoj2)
                        #verificando se algum jogador ficou sem cartas
			if len(mj1) == 0 or len(mj2) == 0:
				break
			rodadas+=1
	#Verifiando condições para o fim do jogador
	if len(maoj1) == 0 or pontosj1 > pontosj2:
		print("Jogador 1 winner")


	elif len(maoj2) == 0 or pontosj2 > pontosj1:
		print("Jogador 2 winner")
		
        #cadastro para guardar o score no banco de dados:
	ler = int(input("Digite 0 para salvar os dados do jogador1:"))
	binario(cadastro(pontosj1),ler)

	ler = int(input("Digite 0 para salvar os dados do jogador2: "))
	binario(cadastro(pontosj2),ler)



print(game())
input()
