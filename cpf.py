"""
CPF = 16899535009
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

cpf = input('Digite apenas os numeros do seu CPF: ')


def verifica_cpf(cpf):
    if cpf.isalpha():
        print('CPF INVÁLIDO, TENTE NOVAMENTE.')

    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for indice in range(19):  # 19 verificações e farei
        if indice > 8:  # quado chegar em oito começo de novo
            indice -= 9

        total = total + int(novo_cpf[indice]) * reverso

        reverso -= 1  # desconto um do contador
        if reverso < 2:  # quando chegar em dois, atribuo 11
            reverso = 11

            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
                total = 0
                novo_cpf += str(digito)
            else:
                total = 0
                novo_cpf += str(digito)

    if novo_cpf == cpf:
        return 'CPF VÁLIDO'

    return 'CPF INVÁLIDO'  # me retorna que é inválido por padrão


print(verifica_cpf(cpf))
