def pressao():
    N = int(input('Qual a pressão desejada? '))
    M = int(input('Qual a pressão lida pela bomba? '))

    if(N<1 or N>40):
        print('Pressão inválida.')
        return

    if(M<1 or M>40):
        print('Pressão inválida.')
        return

    print(N-M)
    return
pressao();
