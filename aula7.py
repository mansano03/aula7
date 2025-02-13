nome   = []
idades = []
emails = []
senhas = []

my_nome, minha_idade, meu_email, minha_senha  =  input('Digite seu nome'),input('Digite sua idade'), input('Digite seu email'),input('Digite sua senha') 

nome.append(my_nome)
idades.append(minha_idade)
emails.append(meu_email)
senhas.append(minha_senha)

print('DADOS INSERIDOS COM SUCESSO!')

print(f'SEJA BEM VINDO(A) {nome[0]}')

dados = (nome[0],idades[0],emails[0],senhas[0])
print(dados)

print('''
Escolha um produto a partir do ID
id 0 - a
id 1 - b
id 2 - c            

''')

menu =  ['a', 'b', 'c']
valores  =  [20.5,150,250]

escolha =  int(input('Digite o ID do Produto: '))

meu_carrinho = []
meu_total =  []

if escolha == 0:
    meu_carrinho.append(menu[escolha])
    meu_total.append(valores[escolha])
    print('.....................')
    print(f'Produto -  {menu[escolha]} valor R$ {valores[escolha]}')
elif escolha == 1:
    meu_carrinho.append(menu[escolha])
    meu_total.append(valores[escolha])
    print('.....................')
    print(f'Produto -  {menu[escolha]} valor R$ {valores[escolha]}')
elif escolha == 2:
    meu_carrinho.append(menu[escolha])
    meu_total.append(valores[escolha])
    print('.....................')
    print(f'Produto -  {menu[escolha]} valor R$ {valores[escolha]}')
else:
    print('Digitação incorreta')     



 

print(f'Total - R$ {valores[escolha]}')





forma_de_pagamento = {
1: "PIX",
2:'CC',
3:'CD',
4:'DINHEIRO'
}


escolha_fr_pag =  int(input('Escolha a forma de pagamento: 1 pix, 2 CC, 3CD, 4 Dinheiro '))

if escolha_fr_pag == 1:
    forma =  forma_de_pagamento[1]
    print(f'Seu pagamento vai ser efetuado em {forma}')
elif escolha_fr_pag == 2:
    forma =  forma_de_pagamento[2]
    print(f'Seu pagamento vai ser efetuado em {forma}')  
elif escolha_fr_pag == 3:
    forma =  forma_de_pagamento[3]
    print(f'Seu pagamento vai ser efetuado em {forma}')
elif escolha_fr_pag == 4:
    forma =  forma_de_pagamento[1]
    print(f'Seu pagamento vai ser efetuado em {forma}')  
else: 
    print('Digite algo valido: ')
    
    
    
    


cliente1_nome = input('Digite o nome do Cliente 1: ')
cliente1_idade = int(input('Digite a idade do Cliente 1: '))

cliente2_nome = input('Digite o nome do Cliente 2: ')
cliente2_idade = int(input('Digite a idade do Cliente 2: '))

cliente3_nome = input('Digite o nome do Cliente 3: ')
cliente3_idade = int(input('Digite a idade do Cliente 3: '))


print('Tipos de Quarto: Simples, Duplo, Luxo')

cliente1_quarto = input('Escolha o quarto para o Cliente 1: ')
cliente2_quarto = input('Escolha o quarto para o Cliente 2: ')
cliente3_quarto = input('Escolha o quarto para o Cliente 3: ')


preco_simples = 100
preco_duplo = 150
preco_luxo = 250

cliente1_dias = int(input(f'Quantos dias o Cliente 1 ({cliente1_nome}) ficará hospedado? '))
cliente2_dias = int(input(f'Quantos dias o Cliente 2 ({cliente2_nome}) ficará hospedado? '))
cliente3_dias = int(input(f'Quantos dias o Cliente 3 ({cliente3_nome}) ficará hospedado? '))


if cliente1_quarto == 'simples':
    valor_cliente1 = preco_simples * cliente1_dias
elif cliente1_quarto == 'duplo':
    valor_cliente1 = preco_duplo * cliente1_dias
else:
    valor_cliente1 = preco_luxo * cliente1_dias

if cliente2_quarto == 'simples':
    valor_cliente2 = preco_simples * cliente2_dias
elif cliente2_quarto == 'duplo':
    valor_cliente2 = preco_duplo * cliente2_dias
else:
    valor_cliente2 = preco_luxo * cliente2_dias

if cliente3_quarto == 'simples':
    valor_cliente3 = preco_simples * cliente3_dias
elif cliente3_quarto == 'duplo':
    valor_cliente3 = preco_duplo * cliente3_dias
else:
    valor_cliente3 = preco_luxo * cliente3_dias


print(f'Cliente 1: {cliente1_nome}, {cliente1_idade} anos, Quarto {cliente1_quarto}, {cliente1_dias} dias')
print(f'Valor Total Cliente 1: R$ {valor_cliente1:.2f}')

print(f'Cliente 2: {cliente2_nome}, {cliente2_idade} anos, Quarto {cliente2_quarto}, {cliente2_dias} dias')
print(f'Valor Total Cliente 2: R$ {valor_cliente2:.2f}')

print(f'Cliente 3: {cliente3_nome}, {cliente3_idade} anos, Quarto {cliente3_quarto}, {cliente3_dias} dias')
print(f'Valor Total Cliente 3: R$ {valor_cliente3:.2f}')
    
    
    
    
    