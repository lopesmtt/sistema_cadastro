import json
from colorama import init, Fore, Style 
init(autoreset=True)

# Variável global que vai manter o usuário logado
usuario_logado = None

# Função para garantir que o admin esteja cadastrado
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
        print(Fore.YELLOW + "Admin cadastrado com sucesso!")

# Função de alteração de senha
def alterar_senha():
    if usuario_logado is None:
        print(Fore.RED + "Você precisa estar logado para alterar a senha.")
        return
    senha_antiga = input("Digite a sua senha antiga: ").strip()
    if senha_antiga != usuario_logado["senha"]:
        print(Fore.RED + "Senha antiga incorreta.")
        return
    nova_senha = input("Digite uma nova senha: ").strip()
    usuario_logado["senha"] = nova_senha
    usuarios = carregar_usuarios()
    for i, usuario in enumerate(usuarios):
        if usuario["email"] == usuario_logado["email"]:
            usuarios[i] = usuario_logado
    salvar_usuarios(usuarios)
    print(Fore.GREEN + "Senha alterada com sucesso.")

# Função para carregar os usuários do arquivo
def carregar_usuarios():
    try:
        with open("users.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
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
        print(Fore.RED + "Erro: Nenhum campo pode estar vazio.")
        return

    usuarios = carregar_usuarios()

    # Verifica se o email já está cadastrado
    if any(user["email"] == email for user in usuarios):
        print(Fore.RED + "Erro: Este email já está cadastrado.")
        return

    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    usuarios.append(novo_usuario)  # Adiciona o novo usuário à lista
    salvar_usuarios(usuarios)  # Salva a lista atualizada de usuários no arquivo
    print(Fore.GREEN + "Usuário cadastrado com sucesso!")

# Função de login
def login_usuario():
    global usuario_logado
    email = input("Digite seu e-mail: ").strip()
    senha = input("Digite sua senha: ").strip()
    
    usuarios = carregar_usuarios()
    
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            usuario_logado = usuario
            print(Fore.BLUE + f"Bem-vindo, {usuario['nome']}\n")
            return
    print(Fore.RED + "Email ou senha incorretos\n")

# Função para remover um usuário
def remover_usuario():
    if usuario_logado is None or usuario_logado["email"] != "admin@admin.com":
        print(Fore.RED + "Acesso negado. Somente admins podem remover usuários.")
        return
    
    email_remover = input("Digite o e-mail do usuário que deseja remover: ").strip()
    usuarios = carregar_usuarios()
    
    usuario_encontrado = False
    
    for i, usuario in enumerate(usuarios):
        if usuario["email"] == email_remover:
            usuarios.pop(i)  # Remove o usuário da lista
            salvar_usuarios(usuarios)  # Salva a lista atualizada de usuários
            print(Fore.GREEN + "Usuário removido com sucesso!")
            usuario_encontrado = True
            break
    
    if not usuario_encontrado:
        print(Fore.RED + "Usuário não encontrado.")

# Função para listar usuários (somente admin)
def listar_usuarios():
    if usuario_logado is None or usuario_logado["email"] != "admin@admin.com":
        print(Fore.RED + "Acesso negado. Somente admins podem listar usuários.")
        return
    
    usuarios = carregar_usuarios()
    print("Lista de usuários:")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")    

def buscar_usuario(users_db, busca):
    """
    Função para buscar um usuário no banco de dados.
    users_db: lista de dicionários com os dados dos usuários.
    busca: nome ou e-mail para procurar.
    """
    resultados = []
    for usuario in users_db:
        if busca.lower() in usuario['nome'].lower() or busca.lower() in usuario['email'].lower():
            resultados.append(usuario)
    
    return resultados

usuarios = [     
    {
        "nome": "matheus",
        "email": "matheusllopes22@gmail.com",
        "senha": "1111"
    },
    {
        "nome": "matheus",
        "email": "email@email.com",
        "senha": "123"
    },
    {
        "nome": "Matheus",
        "email": "matheus@email.com",
        "senha": "123"
    },
    {
        "nome": "Matheus",
        "email": "matheus22@mail.com",
        "senha": "233"
    },
    {
        "nome": "Administrador",
        "email": "admin@admin.com",
        "senha": "admin123"
    },
    {
        "nome": "Joao",
        "email": "joao@333.com",
        "senha": "333"
    }
]

busca = input("Digite o nome ou e-mail para buscar: ")
usuarios_encontrados = buscar_usuario(usuarios, busca)

if usuarios_encontrados:
    for usuario in usuarios_encontrados:
        print(f"Usuário encontrado: {usuario['nome']} - {usuario['email']}")
else:
    print("Nenhum usuário encontrado.")
                                                                                                                                                       
# Função do menu principal
def menu():
    while True:
        print("== Menu ==")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Listar usuário(somente admin)")
        if usuario_logado:
            print(Fore.MAGENTA + "4. Alterar senha")
            print(Fore.MAGENTA + "5. Remover usuário(Somente admin)")
        print("0. Sair")
        opcao = input(Fore.LIGHTCYAN_EX + "Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_usuario()  
        elif opcao == "2":
            login_usuario()
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "4" and usuario_logado:
            alterar_senha()
        elif opcao == "5" and usuario_logado:
            remover_usuario()
        elif opcao == "6" and usuario_logado:
                busca = input("Digite um nome ou email para buscar:    ")
                
        elif opcao == "0":          
            print(Fore.CYAN + "Saindo do sistema...")
            break
        else:
            print(Fore.RED + "Opção inválida.\n")

# Função principal para o sistema
def main():
    print("=== Sistema de Cadastro de Usuários ===")
    garantir_admin()  # Garante que o admin está cadastrado
    menu()

# Rodando o programa
if __name__ == "__main__":
    main()