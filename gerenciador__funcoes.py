def linha(tipo_de_linha):
    q = tipo_de_linha * 40
    return print(q)


def leia_int(msg):
    while True:
        try:
            numero = int(input(msg))
        except Exception:
            print('ERRO! Digite uma opção válida!')
            linha('-=')
            continue
        else:
            return numero


def leia_preco(msg):
    while True:
        try:
            n = float(input(msg))
        except Exception:
            print(f'ERRO! Digite o preço do produto!')
            linha('-=')
            continue
        else:
            return n


def leia_str(msg):
    while True:
        try:
            txt = str(input(msg))
        except Exception:
            print('ERRO! Escreva o nome do produto!')
            linha('-=')
            continue
        else:
            return txt


def leia_lista(msg):
    while True:
        try:
            lista = list(input(msg))
        except Exception:
            print('ERRO! Digite o um CPF válido!')
            linha('-=')
            continue
        else:
            return lista
