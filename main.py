import textwrap

def menu():
  menu = """
  --------------MENU-------------
  [1]\tDepositar
  [2]\tSacar
  [3]\tExtrato
  [4]\tNova Conta
  [5]\tListar Contas
  [6]\t Novo Usuário
  [7]\tSair
  """
  return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f'Depósito:\tR$ {valor:.2f}\n'
    print('\n=== Depósito realizado! ===')
  else:
    print('\n@@@ Operação falhou, valor inválido @@@')
  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques > limite_saques

  if excedeu_saldo:
    print('\n@@@ Operação falhou, saldo insuficiente @@@')

  elif excedeu_limite:
    print('\n@@@ Operação falhou, valor de saque insuficiente @@@') 

  elif excedeu_saques:
    print('\n@@@ Operação falhou, saldo insuficiente @@@')

  elif valor > 0:
    saldo -= valor
    extrato += f'saques\t\tR$ {valor:.2f}\n'
    numero_saques += 1
    print('\n=== Saque realizado com sucesso ===')

  else:
    print('\n@@@ Operação falhou, valor inválido @@@')

















  
  return saldo, extrato

def exibir_extrato(saldo, /,*,extrato):
  print('\n-----------------EXTRATO-----------------')
  print('Não foram realizadas movimentações' if not extrato else extrato)
  print(f'\nSaldo: \t\tR$ {saldo:.2f}')
  print('-------------------------------------------')

def criar_usuario(usuarios):
  cpf = input('informe CPF: ')
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print('@@@ Este CPF já foi cadastrado @@@')
    return

  nome = input('Informe nome completo: ')
  data_nascimento = input('Informe a data de nascimento (dd - mm - aaaa)')
  endereco = input('Informe o endereço (rua, numero, bairro, cidade-SIGLA e Estado): ')

  usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

  print('=== Usuario cadastrado com sucesso ===')

def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']==cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input('Informe o CPF: ')
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print('\n=== Conta criada! ===')
    return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

  print('\n@@@ usuário não encontrado. @@@')
  
def listar_contas(contas):
  for conta in contas:
    linha = f"""\
        agencia:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
    """
    print('= ' * 100)
    print(textwrap.dedent(linha))






def main():
  LIMITE_SAQUE = 3
  AGENCIA = '0001'

  saldo = 0
  limite = 0
  extrato = ''
  numero_saques = 0
  usuarios = []
  contas = []

  while True:
    opcao = menu()

    if opcao == '1':
      valor = float(input('Informe o valor: '))

      saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == '2':
      valor = float(input('Informe o valor do saque: '))

      saldo, extrato = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=LIMITE_SAQUE,
    )

    elif opcao == '3':
      exibir_extrato(saldo, extrato=extrato)
    elif opcao == '6':
      criar_usuario(usuarios)
    elif opcao == '4':
      numero_conta = len(contas)+1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)

    elif opcao == '5':
      listar_contas(contas)

    elif opcao == '7':
      break

    else:
      print('Opçao inválida, informe um comendo válido.')

main()
