import media


def test_media1():
    dicionario = {'maria': [5.0, 10], 'joao': [10, 8.5]}
    assert media.calcular_media(dicionario, 'joao') == 9.25


def test_media2():
    dicionario = {'maria': [5.0, 10], 'joao': [10, 8.5]}
    assert media.calcular_media(dicionario, 'ana') == 0


def test_media3():
    dicionario = {'pedro': [0, 0], 'ana': [5, 8], 'paulo': [5, 7]}
    assert media.calcular_media(dicionario, 'ana') == 6.5


def test_media4():
    dicionario = {'pedro': [0, 0], 'ana': [5, 8], 'paulo': [5, 7]}
    assert not media.calcular_media(dicionario, 'ana') == 0