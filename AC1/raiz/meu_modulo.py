def meu_modulo(n):
    return n * '-'


def linha_dupla(n):
    return n * '='


def linha_simbolo(simbolo, n):
    return str(simbolo) * n


def eh_perfeito(n):
    soma = 0
    if type(n) != int:
        return False

    for i in range(1, n):
        if (n % i) == 0:
            soma += i

    if soma == n:
        return True

    return False
