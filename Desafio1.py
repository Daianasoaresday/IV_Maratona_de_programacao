def medircaixa():
    D = float(input('Diametro da bola de boliche: '))

    A = float(input('Altura da caixa: '))
    L = float(input('Largura da caixa: '))
    P = float(input('Profundidade da caixa: '))

    if (D<1 or D>1000): 
        print('Valor de diametro inválido.')
        return

    if (A<1 or A>1000): 
        print('Valor de diametro inválido.')
        return

    if (L<1 or L>1000): 
        print('Valor de diametro inválido.')
        return

    if (P<1 or P>1000): 
        print('Valor de diametro inválido.')
        return

    if(D>L or D>A or D>P):
        print('N')
        return
    print ('S')
    return

medircaixa();
