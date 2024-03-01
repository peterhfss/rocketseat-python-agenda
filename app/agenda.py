import sys
from controller import *

def menu():

  menu = """
### Agenda de Contatos ###

[1] Adicionar contato
[2] Editar contato
[3] Remover contato
[4] Adicionar contato como favorito
[5] Remover contato como favorito
[6] Contatos cadastrados
[7] Contatos favoritos
[8] Sair da agenda

Escolha uma opção do menu para prosseguir
      
"""

  opcao = input(menu)

  if opcao == '1':
    adicionar_contato()
  elif opcao == '2':
    contato_email = input('\nInforme o email do contato desejado:')
    editar_contato(contato_email)
  elif opcao == '3':
    contato_email = input('\nInforme o email do contato desejado:')
    remover_contato(contato_email)
  elif opcao == '4':
    contato_email = input('\nInforme o email do contato desejado:')
    favoritar_contato(contato_email)
  elif opcao == '5':
    contato_email = input('\nInforme o email do contato desejado:')
    desfavoritar_contato(contato_email)
  elif opcao == '6':
    listar_contatos()
  elif opcao == '7':
    listar_favoritos()
  elif opcao == '8':
    print('\nEncerrando...')
    sys.exit()
  else:
    print('\nOpção inválida!')

while(True):
  menu()