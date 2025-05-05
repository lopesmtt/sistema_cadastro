import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

ARQUIVO_USUARIOS = "users.json"
ARQUIVO_LOG = "logs.txt"

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as file:
            return json.load(file)
    return []

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as file:
        json.dump(usuarios, file, indent=4)

def registrar_log(mensagem):
    with open(ARQUIVO_LOG, "a") as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensagem}\n")

usuarios = carregar_usuarios()
usuario_logado = None

def criar_usuario_admin():
    for u in usuarios:
        if u.get('email') == 'admin@admin.com':
            u['role'] = 'admin'
            salvar_usuarios(usuarios)
            return
    usuarios.append({
        "nome": "Administrador",
        "email": "admin@admin.com",
        "senha": "admin123",
        "role": "admin"
    })
    salvar_usuarios(usuarios)

def cadastrar_usuario():
    def cadastro():
        nome = entry_nome.get().strip()
        email = entry_email.get().strip()
        senha = entry_senha.get().strip()

        if not nome or not email or not senha:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        for u in usuarios:
            if u["email"] == email:
                messagebox.showerror("Erro", "Já existe um usuário com esse e-mail.")
                return

        usuarios.append({"nome": nome, "email": email, "senha": senha, "role": "user"})
        salvar_usuarios(usuarios)
        registrar_log(f"Usuário cadastrado: {email}")
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        cadastro_window.destroy()

    cadastro_window = tk.Toplevel(root)
    cadastro_window.title("Cadastro de Usuário")

    tk.Label(cadastro_window, text="Nome:").pack()
    entry_nome = tk.Entry(cadastro_window)
    entry_nome.pack()

    tk.Label(cadastro_window, text="E-mail:").pack()
    entry_email = tk.Entry(cadastro_window)
    entry_email.pack()

    tk.Label(cadastro_window, text="Senha:").pack()
    entry_senha = tk.Entry(cadastro_window, show="*")
    entry_senha.pack()

    tk.Button(cadastro_window, text="Cadastrar", command=cadastro).pack()

def login_usuario():
    def login():
        global usuario_logado
        email = entry_email.get().strip()
        senha = entry_senha.get().strip()

        for usuario in usuarios:
            if usuario["email"] == email and usuario["senha"] == senha:
                usuario_logado = usuario
                registrar_log(f"Login realizado: {email}")
                messagebox.showinfo("Login", f"Bem-vindo, {usuario['nome']}!")
                login_window.destroy()
                return

        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    login_window = tk.Toplevel(root)
    login_window.title("Login")

    tk.Label(login_window, text="E-mail:").pack()
    entry_email = tk.Entry(login_window)
    entry_email.pack()

    tk.Label(login_window, text="Senha:").pack()
    entry_senha = tk.Entry(login_window, show="*")
    entry_senha.pack()

    tk.Button(login_window, text="Login", command=login).pack()

def listar_usuarios():
    if usuario_logado and usuario_logado["role"] == "admin":
        lista = "\n".join([f"{u['nome']} - {u['email']}" for u in usuarios])
        messagebox.showinfo("Lista de Usuários", lista)
    else:
        messagebox.showerror("Erro", "Você precisa ser um administrador para acessar essa função.")

def alterar_senha():
    if usuario_logado:
        def mudar_senha():
            nova_senha = entry_senha.get().strip()
            if nova_senha:
                usuario_logado['senha'] = nova_senha
                salvar_usuarios(usuarios)
                registrar_log(f"{usuario_logado['email']} alterou a senha.")
                messagebox.showinfo("Alterar Senha", "Senha alterada com sucesso!")
                alterar_senha_window.destroy()
            else:
                messagebox.showerror("Erro", "A senha não pode estar vazia.")

        alterar_senha_window = tk.Toplevel(root)
        alterar_senha_window.title("Alterar Senha")

        tk.Label(alterar_senha_window, text="Nova Senha:").pack()
        entry_senha = tk.Entry(alterar_senha_window, show="*")
        entry_senha.pack()

        tk.Button(alterar_senha_window, text="Alterar", command=mudar_senha).pack()
    else:
        messagebox.showerror("Erro", "Você precisa estar logado para alterar a senha.")

def exibir_dados_usuario():
    if usuario_logado:
        info = f"Nome: {usuario_logado['nome']}\nE-mail: {usuario_logado['email']}\nTipo: {'Administrador' if usuario_logado['role'] == 'admin' else 'Usuário comum'}"
        messagebox.showinfo("Dados do Usuário", info)
    else:
        messagebox.showerror("Erro", "Você precisa estar logado para ver seus dados.")

def editar_dados_usuario():
    if usuario_logado:
        def salvar_alteracoes():
            novo_nome = entry_nome.get().strip()
            novo_email = entry_email.get().strip()

            if novo_nome and novo_email:
                usuario_logado['nome'] = novo_nome
                usuario_logado['email'] = novo_email
                salvar_usuarios(usuarios)
                registrar_log(f"{usuario_logado['email']} atualizou seus dados.")
                messagebox.showinfo("Atualizado", "Dados atualizados com sucesso!")
                editar_window.destroy()
            else:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

        editar_window = tk.Toplevel(root)
        editar_window.title("Editar Dados")

        tk.Label(editar_window, text="Novo nome:").pack()
        entry_nome = tk.Entry(editar_window)
        entry_nome.insert(0, usuario_logado['nome'])
        entry_nome.pack()

        tk.Label(editar_window, text="Novo email:").pack()
        entry_email = tk.Entry(editar_window)
        entry_email.insert(0, usuario_logado['email'])
        entry_email.pack()

        tk.Button(editar_window, text="Salvar", command=salvar_alteracoes).pack()
    else:
        messagebox.showerror("Erro", "Você precisa estar logado.")

def excluir_conta():
    global usuario_logado
    if usuario_logado:
        confirmacao = messagebox.askyesno("Confirmação", "Deseja realmente excluir sua conta?")
        if confirmacao:
            usuarios.remove(usuario_logado)
            registrar_log(f"{usuario_logado['email']} excluiu a conta.")
            salvar_usuarios(usuarios)
            usuario_logado = None
            messagebox.showinfo("Conta Excluída", "Sua conta foi excluída com sucesso.")
    else:
        messagebox.showerror("Erro", "Você precisa estar logado.")

def sair():
    root.quit()

# Interface principal
root = tk.Tk()
root.title("Sistema de Cadastro de Usuários")
root.geometry("400x400")

tk.Label(root, text="=== Sistema de Cadastro ===", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="1. Cadastrar", width=25, command=cadastrar_usuario).pack(pady=5)
tk.Button(root, text="2. Login", width=25, command=login_usuario).pack(pady=5)
tk.Button(root, text="3. Listar usuários (admin)", width=25, command=listar_usuarios).pack(pady=5)
tk.Button(root, text="4. Alterar senha", width=25, command=alterar_senha).pack(pady=5)
tk.Button(root, text="5. Exibir meus dados", width=25, command=exibir_dados_usuario).pack(pady=5)
tk.Button(root, text="6. Editar meus dados", width=25, command=editar_dados_usuario).pack(pady=5)
tk.Button(root, text="7. Excluir minha conta", width=25, command=excluir_conta).pack(pady=5)
tk.Button(root, text="0. Sair", width=25, command=sair).pack(pady=5)

criar_usuario_admin()
root.mainloop()