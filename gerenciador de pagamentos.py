import gerenciador__funcoes
lista = list()
listap = list()
lista_completa = list()
item = vlr = cont = 0
itens = ' '
print(f'{"-" * 30:<30}', f'{"LOJA DO WELLINTON!":^20}', f'{"-" * 30:>30}')
gerenciador__funcoes.linha('-=')
inicio = str(input('Tecle  ENTER  para iniciar!'))
gerenciador__funcoes.linha('-=')
nome = gerenciador__funcoes.leia_int('''
    1- Inserir o CPF
    2- Continuar sem CPF
    ---> ''')
gerenciador__funcoes.linha('-=')
while nome not in [1, 2]:
    nome = gerenciador__funcoes.leia_int('''
    1- Inserir o CPF
    2- Continuar sem CPF
    ---> ''')
    gerenciador__funcoes.linha('-=')
if nome == 1:
    pare = False
    while not pare:
        cpf = gerenciador__funcoes.leia_int('Digite o CPF: ')
        cpf = str(cpf)
        gerenciador__funcoes.linha('-=')
        while len(cpf) != 11:
            print('CPF INVÁLIDO!!!')
            cpf = gerenciador__funcoes.leia_int('Digite o CPF:')
            cpf = str(cpf)
        if len(cpf) == 11:
            arquivo = open('gerenciador_arquivos.txt', 'w')
            fatia_um = cpf[:3]
            fatia_dois = cpf[3:6]
            fatia_tres = cpf[6:9]
            fatia_quatro = cpf[9:11]
            cpf_formatado = f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'
            arquivo.write(cpf_formatado)
            arquivo.close()
            cpfok = gerenciador__funcoes.leia_int(f'''
            O CPF inserido foi: {cpf_formatado}
                Está correto?
                [ 1 ] SIM
                [ 2 ] NÃO
                 -->''')
            while cpfok not in (1, 2):
                print('ERRO! Digite uma opção válida!')
                gerenciador__funcoes.linha('-=')
                cpfok = gerenciador__funcoes.leia_int(f'''
            O CPF inserido foi: {cpf_formatado}
            
                Está correto?
                [ 1 ] SIM
                [ 2 ] NÃO
                 -->''')
            if cpfok == 2:
                pare = False
            else:
                gerenciador__funcoes.linha('-=')
                print('    Vamos às compras!')
                gerenciador__funcoes.linha('-=')
                pare = True
elif nome == 2:
    print('OK')
    cont += 1
    gerenciador__funcoes.linha('-=')
while itens not in u'\ue007':
    item += 1
    itens = gerenciador__funcoes.leia_str(f'PASSE O {item}º ITEM: ').upper()
    prod = gerenciador__funcoes.leia_preco('Valor: R$ ')
    vlr += prod
    print(f'Sub total: R$ {vlr:.2f}')
    gerenciador__funcoes.linha('-=')
    prod = f'{prod:.2f}'
    prod = str(prod).replace('.', ',')
    lista.append(itens)
    listap.append(prod)
    lista.pop()
    listap.pop()
    lista_completa.append(lista)
    lista_completa.append(listap)
    soma = vlr

print('')
arquivo = open('gerenciador_arquivos.txt', 'r')
print(f'Cliente: {arquivo.read()}')
print('')
arquivo.close()
for produto, preco in lista_completa:
    print(produto)
stop = False
desc10 = vlr * 0.1
desc5 = vlr * 0.05
taxa1 = vlr + desc5
taxa2 = vlr + desc10
while not stop:
    print('')
    print(f'{"SUB TOTAL: ":.<30} {"R$"} {vlr:>5.2f}')
    print('')
    if itens in u'\ue007':
        print(f'Total de produtos: {item - 1}')
        print('')
    gerenciador__funcoes.linha('-=')
    print('FORMAS DE PAGAMENTO:')
    pag = gerenciador__funcoes.leia_int('''            
                [ 1 ] DINHEIRO (10% de desconto)
                [ 2 ] CRÉDITO/DÉBITO (5% de desconto)
                [ 3 ] PARCELADO (até 10x com juros)
                
                -->''')
    while pag not in range(1, 4):
        pag = gerenciador__funcoes.leia_int('''
                [ 1 ] DINHEIRO (10% de desconto)
                [ 2 ] CRÉDITO/DÉBITO (5% de desconto)
                [ 3 ] PARCELADO (até 10x com juros)
                        
                --> ''')
    if pag == 1:
        gerenciador__funcoes.linha('-=')
        print(f'''
            Desconto: 10%\nTOTAL COM DESCONTO: R${vlr - desc10:.2f} ''')
    elif pag == 2:
        gerenciador__funcoes.linha('-=')
        print(f'''
            Desconto: 5%\nTOTAL COM DESCONTO: R${vlr - desc5:.2f} ''')
    elif pag == 3:
        parc = gerenciador__funcoes.leia_int('EM QUANTAS VEZES? [ 2x até 10x com juros. ]: ')
        while parc not in range(2, 11):
            print('Opção inválida!')
            print('')
            parc = gerenciador__funcoes.leia_int('Em quantas vezes quer parcelar a compra. [2x até 10x]: ')
        if parc <= 5:
            parctaxa1 = (vlr + desc5) / parc
            gerenciador__funcoes.linha('-=')
            print(f'''
    TOTAL:        \tR${vlr + (desc5):.2f}
    QTD. PARCELA:\t{parc}x
    Tx juros:     \t{desc5:.0f}%
    VLR PARCELA:  \tR${parctaxa1:.2f}
    ''')
            gerenciador__funcoes.linha('-=')
        if parc in range(5, 11):
            parctaxa2 = (vlr + desc10) / parc
            print(f'''
    TOTAL:        \tR${vlr + (desc10):.2f}
    QTD. PARCELA: \t{parc}x
    Tx juros:     \t{desc10:.0f}%
    VLR PARCELA:  \tR${parctaxa2:.2f}
    ''')
    gerenciador__funcoes.linha('-=')
    confirmacao = gerenciador__funcoes.leia_int('''O QUE DESEJA FAZER AGORA?
        
            [ 1 ] FINALIZAR A TRANSAÇÃO
            [ 2 ] VOLTAR PARA PAGAMENTOS
               
             --> ''')
    gerenciador__funcoes.linha('-=')
    while confirmacao not in [1, 2]:
        print('Opção inválida')
        gerenciador__funcoes.linha('-=')
        confirmacao = gerenciador__funcoes.leia_int('''O QUE DESEJA FAZER AGORA?
        
            [ 1 ] FINALIZAR A TRANSAÇÃO
            [ 2 ] VOLTAR PARA PAGAMENTOS
               
             --> ''')
    if confirmacao == 2:
        print('Voltamos ao pagamento!')
        gerenciador__funcoes.linha('-=')
        stop = False
    if confirmacao == 1:
        stop = True
        print('''OPERAÇÃO FINALIZADA COM SUCESSO!
        
        AGRADECEMOS A PREFERÊNCIA!
        
        VOLTE SEMPRE!
        ''')
        print(f'{"-" * 30:<30}', f'{"LOJA DO WELLINTON!":^20}', f'{"-" * 30:>30}')
