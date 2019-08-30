# Linguagem de Programação II
# Atividade Contínua 02
#
# Aluno 1: Henrique Espadaro Serquera - RA: 1802534
# Aluno 2: Israel Felipe Eduardo da Silva - RA: 1900940

'''
Função que recebe um dicionario (chave é o nome do aluno
e valor é uma lista com duas notas) e o nome de um aluno específico.
A função deve retornar a média aritmética do aluno.
Caso a chave não exista no dicionário, deve retornar zero.
Por exemplo:
Se dicionario = {'Maria': [10, 8], 'Joao': [7.5, 9]} e nome = 'Joao',
entao o retorno deve ser 8.25
'''


def calcular_media(dicionario, nome):
    if nome not in dicionario:
        return 0.0

    return sum(dicionario[nome]) / len(dicionario[nome])
