
def main():
    while True:
        print("Sistema de Cadastro de Usuários")
        print("1 - Cadastrar Usuário")
        print("2 - Fazer Login")
        print("3 - Listar Usuários (Admin)")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            cadastrar_usuario(nome, email, senha)
        elif opcao == "2":
            email = input("Digite seu email para login: ")
            senha = input("Digite sua senha: ")
            if login(email, senha):
                print("Login bem-sucedido!")
            else:
                print("Login falhou!")
        elif opcao == "3":
            listar_usuarios()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()