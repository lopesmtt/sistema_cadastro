import json

usuario_logado = None

#Funçao para garantir que o admin esteja cadastrado
def garantir_admin():
        usuarios = carregar_usuarios()
        
        if not any(user["email"] == "admin@admin.com" for user in usuarios):
            admin = {
                "nome": "Administrador",
                "email": "admin@admin.com",
                "senha": "admin123"
            }
            usuarios.append(admin)
            
            salvar_usuarios(usuarios)
            
            print("Admin cadastrado com sucesso! ")
                 



#Funçao para criar login
def login_usuario():
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        
        try:
             with open("users.json", "r") as arquivo: 
                 usuarios = json.load(arquivo)
        except FilleNotFoundError:
                  print("Nenhum usuario cadastrado ainda")
                  return
        for usuario in usuarios:
            if usuario["e-mail"]== email and usuario["senha"] == senha: 
                print(f"Bem vindo, {usuario['nome']} ! ")
                return 
              
        print("Email ou senha incorretos")                                               


# Função para carregar os usuários do arquivo
def carregar_usuarios():
    try:
        with open("users.json", "r") as arquivo:  # Corrigido: espaço extra removido
            return json.load(arquivo)
    except FileNotFoundError:  # Corrigido: erro de digitação em 'FilleNotFoundError'
        return []  # Se o arquivo não existir, retorna uma lista vazia

# Função para salvar os usuários no arquivo
def salvar_usuarios(lista_usuarios):
    with open("users.json", "w") as arquivo:
        json.dump(lista_usuarios, arquivo, indent=4)

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    if not nome or not email or not senha:  # Verifica se algum campo está vazio
        print("Erro: Nenhum campo pode estar vazio.")
        return

    usuarios = carregar_usuarios()

    # Verifica se o email já está cadastrado
    if any(user["email"] == email for user in usuarios):
        print("Erro: Este email já está cadastrado.")
        return

    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    usuarios.append(novo_usuario)  # Adiciona o novo usuário à lista

    salvar_usuarios(usuarios)  # Salva a lista atualizada de usuários no arquivo
    print("Usuário cadastrado com sucesso!")


#Funçao criar login
def login_usuario():
    global usuario_logado
    email = input("Digite seu e-mail: ").strip()  # .strip() remove espaços extras
    senha = input("Digite sua senha: ").strip()  # .strip() remove espaços extras
    
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            usuario_logado = usuario
            print(f"Bem-vindo, {usuario['nome']}\n")
            return
    print("Email ou senha incorretos\n")

def menu():
        while True:
            print("== Menu == ")
            print("1.  Cadastrar ")
            print("2. Login ")
            print("3. Listar usuario(somente admin)")
            print ("4. Sair ")
            opcao = input("Escolha uma opçao: ").strip() 
            
            if opcao == "1":
                  cadastrar_usuario()  
            elif opcao == "2":
                  login_usuario()
            elif opcao == "3":
                  listar_usuarios()
            elif opcao == "4":
                 print("Saindo do sistema... ")
                 break
            else:
                     print("Opçao Invalida.\n")
                                                                  
                                             
#Funçao listar usuarios(somente admins)
def listar_usuarios():
    if usuario_logado is None or usuario_logado["email"] != "admin@admin.com":
        print("Acesso negado. Somente admins podem listar usuários.")
        return
    
    usuarios = carregar_usuarios()
    print("Lista de usuários:")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")    
                    




# Função principal para o sistema
def main():
    print("=== Sistema de Cadastro de Usuários ===")
    menu()

# Rodando o programa
if __name__ == "__main__":
    main()