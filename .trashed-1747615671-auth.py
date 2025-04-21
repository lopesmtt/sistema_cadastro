import json
from utils import carregar_usuarios, salvar_usuarios

def cadastrar_usuario():
    usuarios = carregar_usuarios()  # Carrega os usuários do arquivo JSON
    nome = input("Digite o nome: ").strip()
    email = input("Digite o email: ").strip()
    senha = input("Digite a senha: ").strip()
    
    # Verifica se algum campo está vazio
    if not nome or not email or not senha:
        print("Nenhum campo pode estar vazio.")
        return
    
    # Verifica se o email já está cadastrado
    for usuario in usuarios:
        if usuario['email'] == email:
            print("Email já cadastrado.")
            return
    
    # Adiciona o novo usuário à lista de usuários
    usuarios.append({"nome": nome, "email": email, "senha": senha})
    
    # Salva a lista atualizada de usuários
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def login_usuario():
    usuarios = carregar_usuarios()  # Carrega os usuários do arquivo JSON
    email = input("Digite o email: ").strip()
    senha = input("Digite a senha: ").strip()
    
    # Verifica se o email e a senha estão corretos
    for usuario in usuarios: 
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f"Bem-vindo, {usuario['nome']}!")
            return True  # Retorna True para indicar que o login foi bem-sucedido
    
    # Caso o login falhe
    print("Email ou senha incorretos.")
    return False  # Retorna False para indicar falha no login