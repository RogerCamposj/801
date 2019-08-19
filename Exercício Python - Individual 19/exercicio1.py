numeros = [2, 3, 4, 5, 6]


def numerologo():
    for numero in numeros:
        if numero % 2 == 0:
            print('o número ' + str(numero) + ' é PAR irmão')


    for numero in numeros:
        if numero % 2 != 0:
            print('o número ' + str(numero) + ' fé ÍMPAR irmão')



if numeros:
    numerologo()
