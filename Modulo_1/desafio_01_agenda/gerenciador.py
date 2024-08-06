def adicionar_contato(agenda, nome_contato, telefone_contato, email):
  contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email, "favorito": False}  
  agenda.append(contato)
  print(f"\nContato {nome_contato} adicionado com sucesso!")
  return

def ver_contatos(agenda):
  print("\nContatos:")
  for indice, contato in enumerate(agenda, start=1):
    favorito = "⭐" if contato["favorito"] else " "
    print(f"{indice}. [ {favorito}] {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']}")
  return

def editar_contato(agenda, indice_contato, nome_contato, telefone_contato, email):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
    agenda[indice_contato_ajustado]["nome"] = nome_contato
    agenda[indice_contato_ajustado]["telefone"] = telefone_contato
    agenda[indice_contato_ajustado]["email"] = email
    print(f"\nDados do contato {indice_contato} atualizados!")
  return

def marcar_desmarcar_favorito(agenda, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  favorito_contato = agenda[indice_contato_ajustado]["favorito"]
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
    favorito_contato = not favorito_contato
    agenda[indice_contato_ajustado]["favorito"] = favorito_contato
    print(f"Status de favorito do Contato {indice_contato} alterado")
  return

def ver_contatos_favoritos(agenda):
  print("\nContatos Favoritos:")
  for indice, contato in enumerate(agenda, start=1):
    if contato["favorito"]:
      print(f"{indice}. {contato['nome']} - Telefone: {contato['telefone']} - Email: {contato['email']}")
  return

def deletar_contato(agenda, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda):
    del agenda[indice_contato_ajustado]
    print(f"\nContato {indice_contato} deletado com sucesso!")
  return

agenda = []
while True:
  print("\nMenu do Gerenciador da Agenda:")
  print("1. Adicionar Contato")
  print("2. Ver Contatos")
  print("3. Editar Contato")
  print("4. Marcar/Desmarcar Contato como Favorito")
  print("5. Ver Contatos Favoritos")
  print("6. Deletar Contato")
  print("7. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_contato = input("\nDigite o nome do contato:")
    telefone_contato = input("Digite o telefone do contato:")
    email_contato = input("Digite o email do contato:")
    adicionar_contato(agenda, nome_contato, telefone_contato, email_contato)

  elif escolha == "2":
    ver_contatos(agenda)

  elif escolha == "3":
    ver_contatos(agenda)
    indice_contato = input("Digite o índice do contato que deseja editar:")
    nome_contato = input("Digite o novo nome do contato:")
    telefone_contato = input("Digite o novo telefone do contato:")
    email_contato = input("Digite o novo email do contato:")
    editar_contato(agenda, indice_contato, nome_contato, telefone_contato, email_contato)

  elif escolha == "4":
    ver_contatos(agenda)
    indice_contato = input("Digite o índice do contato que deseja marcar/desmarcar como favorito:")
    marcar_desmarcar_favorito(agenda, indice_contato)
  
  elif escolha == "5":
    ver_contatos_favoritos(agenda)
  
  elif escolha == "6":
    ver_contatos(agenda)
    indice_contato = input("Digite o índice do contato que deseja deletar:")
    deletar_contato(agenda, indice_contato)

  elif escolha == "7":
    break

print("Programa finalizado")