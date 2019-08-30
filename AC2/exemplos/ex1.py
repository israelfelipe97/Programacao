def intercala(tupla1, tupla2):
    tamanho_maior = 0
    tamanho_menor = 0

    if len(tupla1) >= len(tupla2):
        tamanho_maior = len(tupla1)
        tamanho_menor = len(tupla2)
        tupla_maior = tupla1
    else:
        tamanho_maior = len(tupla2)
        tamanho_menor = len(tupla1)        
        tupla_maior = tupla2

    tupla3 = ()

    for i in range(tamanho_menor):
        tupla3 += (tupla1[i], )
        tupla3 += (tupla2[i], )
    if tamanho_maior != tamanho_menor:
        for i in range(tamanho_menor, tamanho_maior):
            tupla3 += (tupla_maior[i], )

    return tupla3


tupla1 = (1, 2, 3, 4)
tupla2 = (1, 2, 3, 4, 5, 6)
print(intercala(tupla1, tupla2))
