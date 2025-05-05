def buscar_usuario(users_db, busca):
    resultados = []
    for usuario in users_db:
        if busca.lower() in usuario['nome'].lower() or busca.lower() in usuario['email'].lower():
            resultados.append(usuario)
    return resultados