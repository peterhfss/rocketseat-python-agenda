# criando lista de contatos vazia
agenda = []

# funcão de adicionar um novo contato na agenda
def adicionar_contato():
  nome = input('\nDigite o nome do contato:')
  telefone  = input('Digite o número do contato:')
  email = input('Digite o email do contato:')
  favorito = False

  contato = {"nome":nome, "telefone":telefone, "email":email, "contato_favorito":favorito}

  agenda.append(contato)
  print('\nContato salvo com sucesso!')

# funcão de editar contato na agenda a partir do email informado
def editar_contato(email):
  id_antigo_contato = buscar_contato(email)

  if id_antigo_contato == "":
    print('\nContato não encontrado')
  else:
    nome = input('\nDigite o nome do novo contato:')
    telefone  = input('Digite o número do novo contato:')
    email = input('Digite o email do novo contato:')
    favorito = False

    novo_contato = {"nome":nome, "telefone":telefone, "email":email, "contato_favorito":favorito}

    agenda[id_antigo_contato] = novo_contato
    print('\nContato alterado com sucesso!')

# funcão de remover contato na agenda a partir do email informado
def remover_contato(email):
  id_contato = buscar_contato(email)

  if id_contato == "":
    print('\nContato não encontrado')
  else:
    agenda.pop(id_contato)
    print('\nContato removido com sucesso!')

# funcão de exibir todos os contatos adicionados na agenda
def listar_contatos():

  if not agenda:
    print('\nA agenda esta vazia!')
  else:
    print('\nLista de Contatos \n')
    for contato in agenda:
      print(f'Nome:{contato['nome']} \nTelefone:{contato['telefone']} \nEmail:{contato['email']} \nFavorito:{contato['contato_favorito']}')
      print("----------")

# funcão de adicionar o contato como favorito
def favoritar_contato(email):
  mensagem = ""
  for contato in agenda:
    if contato['email'] == email :
      if contato['contato_favorito'] == False:
        contato['contato_favorito'] = True
        mensagem = '\nContato adicionado como favorito!'
    else:
      mensagem = '\nContato não encontrado'
  return print(mensagem)

# funcão de remover o contato como favorito
def desfavoritar_contato(email):
  mensagem = ""
  for contato in agenda:
    if contato['email'] == email :
      if contato['contato_favorito'] == True:
        contato['contato_favorito'] = False
        mensagem = '\nContato removido como favorito!'
    else:
      mensagem = '\nContato não encontrado'
  return print(mensagem)

# funcão de listar somente os contatos favoritos
def listar_favoritos():
  lista_favoritos = []

  for contato in agenda:
    if contato['contato_favorito'] == True:
      lista_favoritos.append(contato)

  if not lista_favoritos:
    print('\nNão existe contatos favoritos')
  else:
    print('\nLista de Contatos Favoritos \n')
    for contato in lista_favoritos:
      print(f'Nome:{contato['nome']} \nTelefone:{contato['telefone']} \nEmail:{contato['email']} \nFavorito:{contato['contato_favorito']}')
      print("----------")

# funcão de pesquisar um contato pelo email
def buscar_contato(email):
  id = ""
  for contato in agenda:
    if contato['email'] == email:
      id = agenda.index(contato)
  return id