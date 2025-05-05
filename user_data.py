import json
from colorama import Fore

def carregar_usuarios():
    try:
        with open("users.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_usuarios(lista_usuarios):
    with open("users.json", "w") as arquivo:
        json.dump(lista_usuarios, arquivo, indent=4)

def garantir_admin():
    usuarios = carregar_usuarios()
    if not any(user["email"] == "admin@admin.com" for user in usuarios):
        usuarios.append({
            "nome": "Administrador",
            "email": "admin@admin.com",
            "senha": "admin123"
        })
        salvar_usuarios(usuarios)
        print(Fore.YELLOW + "Admin cadastrado com sucesso!")