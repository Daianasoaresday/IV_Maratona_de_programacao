def usobomba():

    N = int(input('Número de células do tabuleiro: '))
    if(N < 1 or N > 50):
        print('Valor inválido.')
        return

    tabuleiro1 = []
    tabuleiro2 = []
    for x in range(N):
        tabuleiro1.append(int(input('Tem bomba(0/1)? ')))
        

    for x in range(N):
        valor = 0
        valor += tabuleiro1[x]
        if(x>0):
            valor += tabuleiro1[x-1]
        if(x+1 < len(tabuleiro1)):
            valor += tabuleiro1[x+1]

        tabuleiro2.append(valor)

    for x in tabuleiro2:
        print(x)

usobomba();
