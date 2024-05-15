# Jogo da Disputa

## Descrição do Jogo
O Jogo da Disputa é um jogo de cartas multiplayer offline com limite de dois jogadores por partida. Cada carta possui quatro atributos: valor, força, energia e jokenpô. O objetivo é vencer mais rodadas do que o oponente ao longo de dez rodadas.

## Regras do Jogo
1. Cada jogador recebe um deck embaralhado contendo 5 cartas.
2. Os jogadores alternam escolhendo um atributo para disputar a rodada.
3. Existem dois modos de jogo: aleatório e manual.
   - No modo aleatório, as cartas são ordenadas em ordem crescente de acordo com o atributo escolhido, exceto para o jokenpô.
   - No modo manual, as cartas são sempre ordenadas em ordem alfabética.
4. A disputa é resolvida com base no atributo escolhido. Em caso de empate, são usadas as regras tradicionais do jokenpô.
5. O jogador vencedor descarta a carta utilizada, enquanto o perdedor descarta sua carta e pega uma nova do deck.
6. O jogo termina após 10 rodadas, e o jogador com mais vitórias é declarado vencedor.

## Desenvolvimento
Durante o desenvolvimento do jogo, enfrentamos diversos desafios, incluindo:
- Escolha do formato do baralho de cartas.
- Implementação do cadastro de jogadores e armazenamento em arquivos binários.
- Desenvolvimento do algoritmo de ordenação das cartas de acordo com o atributo selecionado.
- Embaralhamento das cartas.
- Simulação de pilha para distribuição e descarte das cartas.
- Implementação das regras do jokenpô.

## Métodos e Bibliotecas Utilizados
- Utilizamos listas e listas aninhadas para representar o baralho e as cartas.
- Para manipulação de arquivos binários, empregamos as bibliotecas pickle para escrita e leitura.
- O algoritmo de ordenação foi implementado com base no Bubble Sort.
- O embaralhamento das cartas foi realizado utilizando a biblioteca random.
- Para simulação de pilha, utilizamos o método pop() para retirar e adicionar cartas.
- As regras do jokenpô foram implementadas com uma série de condicionais (if, elif, else).

## Como Jogar
1. Clone o repositório em sua máquina local.
2. Execute o script do jogo.
3. Siga as instruções para selecionar o modo de jogo e começar a jogar.

