#1. Cadastro de CPF


#Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"

cpf = input('Insira seu CPF (digite apenas números)')
if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Insira seu CPF (digite apenas números')



#A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços do CPF que o cliente inserir e, uma vez retirados pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.

#No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF correto já só com número.

cpf = input('Insira seu CPF')

#tratar o cpf

#tirar espaço no inicio e no final
cpf = cpf.strip()
#tirar os . (pontos)
cpf = cpf.replace('.', '')
#tirar os traços(-)
cpf = cpf.replace('-', '')
if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Insira seu CPF (digite apenas números')


#Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
#Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido
#Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String. Você pode testar o que ele dá como resposta caso ele não encontre um item dentro da string

nome = input('Digite se nome')
email = input('Digite o seu e-mail')

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluido')
    else:
        print('email invalido')
else:
    print('Digite seu nome e email corretamente')