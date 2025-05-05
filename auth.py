from user_data import carregar_usuarios, salvar_usuarios
from colorama import Fore
import bcrypt

usuario_logado = None

def get_usuario_logado():
    global usuario_logado
    return usuario_logado

def set_usuario_logado(usuario):
    global usuario_logado
    usuario_logado = usuario

def cadastrar_usuario():
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    if not nome or not email or not senha:
        print(Fore.RED + "Erro: Nenhum campo pode estar vazio.")
        return

    usuarios = carregar_usuarios()

    if any(user["email"] == email for user in usuarios):
        print(Fore.RED + "Erro: Este email já está cadastrado.")
        return

    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

    usuarios.append({"nome": nome, "email": email, "senha": senha_hash})
    salvar_usuarios(usuarios)
    print(Fore.GREEN + "Usuário cadastrado com sucesso!")

def login_usuario():
    email = input("Digite seu e-mail: ").strip()
    senha = input("Digite sua senha: ").strip()

    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["email"] == email:
            if bcrypt.checkpw(senha.encode(), usuario["senha"].encode()):
                set_usuario_logado(usuario)
                print(Fore.BLUE + f"Bem-vindo, {usuario['nome']}\n")
                return
            else:
                break
    print(Fore.RED + "Email ou senha incorretos\n")

def alterar_senha():
    usuario = get_usuario_logado()
    if usuario is None:
        print(Fore.RED + "Você precisa estar logado para alterar a senha.")
        return

    senha_antiga = input("Digite a sua senha antiga: ").strip()
    if not bcrypt.checkpw(senha_antiga.encode(), usuario["senha"].encode()):
        print(Fore.RED + "Senha antiga incorreta.")
        return

    nova_senha = input("Digite uma nova senha: ").strip()
    senha_hash = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt()).decode()
    usuario["senha"] = senha_hash

    usuarios = carregar_usuarios()
    for i, u in enumerate(usuarios):
        if u["email"] == usuario["email"]:
            usuarios[i] = usuario

    salvar_usuarios(usuarios)
    print(Fore.GREEN + "Senha alterada com sucesso.")