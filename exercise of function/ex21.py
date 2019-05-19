texto = "reviver"


def func(texto):
    for i in range(len(texto)):
        invertido = texto[::-1]

        def ehpalindromo(invertido, texto):
            if texto == invertido:
                return ("É palíndromo")
            else:
                def naoehpalindromo(invertido, texto):
                    if texto != invertido:
                        return ("Não é palíndromo")
            return (naoehpalindromo(invertido, texto))

    return (ehpalindromo(invertido, texto))


print(func(texto))