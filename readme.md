# API Blog

Este projeto é uma API para um blog simples, permitindo gerenciamento de Categorias, Posts e upload de imagens para os posts. Foi desenvolvido com Django Rest Framework e utiliza SQLite como banco de dados.

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.8+
- **Framework:** Django com Django Rest Framework
- **Banco de Dados:** SQLite

## 📌 Pré-requisitos

Antes de rodar o projeto, certifique-se de que as dependências estão instaladas corretamente e que o ambiente de desenvolvimento está configurado.

### 1️⃣ Instalação das Dependências

Certifique-se de ter o Python 3.8+ e o `pip` instalados. Para instalar as dependências do projeto, execute:

```sh
pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias, conforme listadas no arquivo `requirements.txt`.

### 2️⃣ Acessando o Diretório do Projeto

Navegue até o diretório onde o projeto Django está localizado:

```sh
cd blogsystem/
```

### 3️⃣ Rodando o Servidor

Antes de iniciar o servidor, aplique as migrações do banco de dados:

```sh
python manage.py migrate
```

Agora, inicie o servidor local:

```sh
python manage.py runserver
```

A API estará disponível em **http://127.0.0.1:8000/**.

### 4️⃣ Listando as Rotas Disponíveis

Para visualizar as rotas registradas na API, execute:

```sh
python manage.py show_urls
```

## 💡 Dicas de Desenvolvimento

Para uma melhor experiência, recomendamos o uso do **pyenv** para gerenciar versões do Python e do **virtualenv** para criar ambientes virtuais isolados.

### 🔹 Instalando o pyenv (se necessário)

Caso ainda não tenha o `pyenv`, siga as instruções [neste link](https://github.com/pyenv/pyenv#installation).

Após a instalação, use o `pyenv` para configurar a versão correta do Python:

```sh
pyenv install 3.8.0
pyenv local 3.8.0
```

Isso garantirá que você está utilizando a versão correta do Python no ambiente do projeto.

---

📌 **Observação:** Este projeto foi desenvolvido como uma API simples para estudos e pode ser expandido conforme necessário.

