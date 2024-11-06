
# Organização de Listas Telefônicas

Este projeto consiste na organização dos dados de usuários e suas respectivas linhas telefônicas, nas quais possue dois objetos distintos, com objetivo de  simular um cenário de manipulação/controle de dados para sistemas de telecomunicações. 

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.


### 📋 Pré-requisitos

## Linguagem: Python3

## Sugestão de ambiente: Em momentos que não tiver como configurar o ambiente em windows, linux ou mac, poderá utilizar o [colab python](https://colab.research.google.com/)

Quais são algumas das principais configurações necessárias para instalação do python3?
Segundo esta  [Documentação](https://docs.python.org/pt-br/3/using/configure.html):
```
Recursos e versões mínimas necessários para construir o CPython:

Um compilador C11. Não são necessários recursos opcionais do C11.

No Windows, é necessário o Microsoft Visual Studio 2017 ou posterior.

Suporte para números de ponto flutuante do IEEE 754 e Not-a-Number (NaN) de ponto flutuante.

Suporte a threads.

OpenSSL 1.1.1 é a versão mínima e OpenSSL 3.0.9 é a versão mínima recomendada para os módulos de extensão ssl e hashlib.

SQLite 3.15.2 para o módulo de extensão sqlite3.

Tcl/Tk 8.5.12 para o módulo tkinter.

Autoconf 2.71 e aclocal 1.16.5 são necessários para regenerar o script configure.
```

### 🔧 Instalação

Para baixar este projeto basta [clonar](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository) o repositório pelo github.

Exemplo com SSH:

```
git clone git@github.com:lirasusejdev/listas-python.git 
```


## ⚙️ Sobre o projeto

A proposta será resolver um problema: organizar os dados. Foi proposto receber  através da variável chamada ```data```  que contem as informações de usuários e suas linhas telefônicas, sendo necessario separar esta estrutura abaixo:

```
data = [
 "Bob, bob@xyzzzzzz.com, Rua 12 de Abril, +5500000000000, 40GB",
 "Alice, alice@xyzzzzzz.com, Rua Brasil, +5500111111111, 10GB"
]
```

### 🔩 Analises e propostas

De maneira prática e objetiva foi criado as seguintes propostas no arquivo main.py:

1. Coleta dos dados dos usuários através de uma lista - array com ID, nome, email e endereço.
2. Coleta dos dados telefônicos dos usuários através de uma lista - array com ID, número e plano.
3. Criado a função para exibir as informações - imprimindo e exibindo a frase formatada com as variáveis.
4. Chamada da função para exibir os dados. 

```
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
```




## 📦 Implantação e execução do projeto

Para executar, será necessário rodar no terminal o seguinte comando abaixo:

```
python3 main.py
```
Este comando  ao ser executado, vai rodar o arquivo main.py (principal) que compilará os dados
dando o retorno na frase formatada.

## 🛠️ Construído com ...

Durante o processo de criação, obtinha apenas um chromebook, nas quais não comporta capacidade de armazenamento para toda uma estrutura de instalações de packages e VSCODE ou outra IDE - como no linux, windows e mac.
Neste caso foi utilizado o Github online - pressionando o "ponto" para abrir na nuvem através do repositório. Foi testado e compilado pelo [Colab Python](https://colab.research.google.com/) e também pelo [ONLINE GDB](https://www.onlinegdb.com/online_python_compiler) para gerar os resultados. Para criação de packages complexos em python recomenda-se a instação de toda estrutura - como exemplo nesta documentação: [Instalar pacotes em um ambiente virtual usando pip e venv](https://packaging.python.org/pt-br/latest/guides/installing-using-pip-and-virtual-environments/).

* [ONLINE GDB](https://www.onlinegdb.com/online_python_compiler) - compliador utilizado




## ✒️ Autores


* **Lis Regine Amaral** - *Developer* - [github](https://github.com/lirasusejdev)
