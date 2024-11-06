# Dados de usuários
usuarios = [
    {"id": 1, "nome": "Bob", "email": "bob@xyzzzzzz.com", "endereco": "Rua 12 de Abril"},
    {"id": 2, "nome": "Alice", "email": "alice@xyzzzzzz.com", "endereco": "Rua Brasil"},
]

# Dados das linhas telefônicas
telefones = [
    {"usuario_id": 1, "numero": "+5500000000000", "plano": "40GB"},
    {"usuario_id": 2, "numero": "+5500111111111", "plano": "10GB"},
]



# Função para exibir as informações formatadas
def exibir_dados():
    for usuario in usuarios:
        # Encontrar o telefone e Plano do usuário baseado no 'id'
        telefone = next(tel['numero'] for tel in telefones if tel['usuario_id'] == usuario['id'])
        plano_usuario = next(pl['plano'] for pl in telefones if pl['usuario_id'] == usuario['id'])

        
        # Exibir a frase formatada
        print(f"O cliente, {usuario['nome']}, com email, {usuario['email']}, morador do endereço, {usuario['endereco']}, dono da linha, {telefone} com plano contratado de {plano_usuario}")

# Chamar a função para exibir os dados
exibir_dados()