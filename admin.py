from user_data import carregar_usuarios, salvar_usuarios
from auth import get_usuario_logado
from colorama import Fore

def listar_usuarios():
    usuario_logado = get_usuario_logado()
    if usuario_logado is None or usuario_logado["email"] != "admin@admin.com":
        print(Fore.RED + "Acesso negado. Somente admins podem listar usuários.")
        return

    usuarios = carregar_usuarios()
    print("Lista de usuários:")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")

def remover_usuario():
    usuario_logado = get_usuario_logado()
    if usuario_logado is None or usuario_logado["email"] != "admin@admin.com":
        print(Fore.RED + "Acesso negado. Somente admins podem remover usuários.")
        return

    email_remover = input("Digite o e-mail do usuário que deseja remover: ").strip()
    usuarios = carregar_usuarios()

    for i, usuario in enumerate(usuarios):
        if usuario["email"] == email_remover:
            usuarios.pop(i)
            salvar_usuarios(usuarios)
            print(Fore.GREEN + "Usuário removido com sucesso!")
            return

    print(Fore.RED + "Usuário não encontrado.")