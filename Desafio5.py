def copa(): 
    M = 0
    N = 0

    times = ["A","B","C", "D","E","F","G","H","I","J","K","L","M","N","O","P"]
    times2 = ['']
    times3 = ['']
    times4 = ['']

    for x in range(15):
        M, N = input("Resultado do jogo: ").split(" ", 1)
        M = int(M)
        N = int(N)

        # if de valor dos M N
        if(N<0 or N>20):
            print('Valor inválido.')
            return

        if(M<0 or M>20):
            print('Valor inválido.')
            return

        if(M == N):
            print('Valor inválido.')
            return

        if(x<8):
            if(M > N): 
                times2.append(times[(x*2)])
            else:
                times2.append(times[(x*2)+1])
        elif(x<12):
            if(M > N): 
                times3.append(times2[( (x-8)*2)+1])
            else:
                times3.append(times2[((x-8)*2)+2])
        elif(x<14):
            if(M > N): 
                times4.append(times3[((x-12)*2)+1])
            else:
                times4.append(times3[((x-12)*2)+2])
        else: 
            if(M > N): 
                print(times4[1])
                return
            print(times4[2])

copa();
