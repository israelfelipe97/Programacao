def conta_vogais(s):
    d = {}
    s = s.lower()
    for c in s:

        if c in "aeiou":

            if c in d:
                d[c] += 1
            else:
                d[c] = 1

    return d

print(conta_vogais("Testando"))