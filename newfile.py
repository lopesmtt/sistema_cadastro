import json

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

# Função principal para o sistema
def main():
    print("=== Sistema de Cadastro de Usuários ===")
    cadastrar_usuario()

# Rodando o programa
if __name__ == "__main__":
    main()