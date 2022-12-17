def teve():
    V = int(input('Volume inicial: '))
    T = int(input('Número de trocas: '))

    if(V<0 or V>100):
        print('Valor inválido.')
        return

    if(T<0 or T>1000):
        print('Valor inválido.')
        return
    
    for x in range(T):
        A_i = int(input('Modificação: '));
        if(T<-100 or T>100):
            print('Valor inválido.')
            return
        V+= A_i
        if(V>100):
            V = 100
        elif(V<0):
            V = 0
    
    print(V)
    return
teve();
