"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

# Recebo um cnpj por input do usuário
cnpj = input('Digite um CNPJ: ')


# Remove caracteres especiais deixando apenas os números
def remove_caracteres(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


# Pego o CNPJ resultante da função que removeu os caracteres e removo os dois últimos digitos.
def remove_digitos(cnpj):
    cnpj_sem_digito = remove_caracteres(cnpj[:-2])
    return cnpj_sem_digito


# Multiplico cada numero do cnpj (sem o digito) com o contador reverso
def multiplica_reverso(cnpj_sem_digito):

    # Verifico o tamanho do cnpj atual para definir qual digito calcular
    reverso = len(cnpj_sem_digito)
    # se for o primeiro digito reverso inicia em 5
    if reverso == 12:
        reverso = 5
    # Se for o segundo digito reverso se inicia em 6
    if reverso == 13:
        reverso = 6

    # Crio uma lista vazia para salvar os números multiplicados
    numeros = []

    # para cada numero no meu cnpj sem digito
    for numero in cnpj_sem_digito:
        # print(numero, reverso, numeros)
        # multiplico o número pelo contador reverso e o adiciono na lista
        numeros.append(int(numero) * reverso)
        # Reverso -1 a cada volta do meu laço
        reverso -= 1
        # Quando reverso chegar a 1 atribui nove ao seu valor e recomeço.
        if reverso == 1:
            reverso = 9

    # retorno a soma de todos os numeros multiplicados adicionados a lista.
    return sum(numeros)


# Calcula o digito
def calcula_digito(total):
    # Fórmula com o resultado da função multiplica revorso
    digito = 11 - (total % 11)

    if digito > 9:
        digito = 0

    return digito


def adiciona_digito(numeros, digito):
    # variavel cnpj parcial concatena numeros do cnpj passado com o dig
    cnpj_parcial = str(numeros) + str(digito)

    return cnpj_parcial


def valida():
    # Atribui minha função a uma varivavel
    cnpj_sem_digito = remove_digitos(cnpj)
    # acho o total do primeiro digito
    total_primeiro_digito = multiplica_reverso(cnpj_sem_digito)
    # Calculo o dig e o adiciono ao cnpj sem digitos
    novo_cnpj = adiciona_digito(cnpj_sem_digito,
                                calcula_digito(total_primeiro_digito))

    # verifico se bate com o cnpj original
    if len(novo_cnpj) != cnpj:
        # se não, faço o calculo do seg digito e o adiciono ao cnpj parcial
        total_segundo_digito = multiplica_reverso(novo_cnpj)
        novo_cnpj = adiciona_digito(novo_cnpj, calcula_digito(total_segundo_digito))
    # verifico se o cnpj gerado é igual ao passado
    if novo_cnpj == remove_caracteres(cnpj):
        return 'CNPJ Válido'

    return 'CNPJ Inválido'


print(valida())
