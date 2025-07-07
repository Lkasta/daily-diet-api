# Daily Diet API
Desafio 02 Python Rocketseat

### Regras da aplicação

- Deve ser possível registrar uma refeição feita, com as seguintes informações:
    - Nome
    - Descrição
    - Data e Hora
    - Está dentro ou não da dieta
- Deve ser possível editar uma refeição, podendo alterar todos os dados acima
- Deve ser possível apagar uma refeição
- Deve ser possível listar todas as refeições de um usuário
- Deve ser possível visualizar uma única refeição
- As informações devem ser salvas em um banco de dados

#

# 📚 Dependências do Projeto Flask

Este projeto utiliza as seguintes bibliotecas Python para construção de uma aplicação web com autenticação e banco de dados PostgreSQL:

---

### 🔹 Flask
Micro framework web em Python. Fornece as ferramentas básicas para criar aplicações web, incluindo sistema de rotas, requisições e respostas HTTP, e suporte a extensões.

---

### 🔹 Flask-SQLAlchemy
Extensão que integra o SQLAlchemy ao Flask. Permite definir modelos ORM (Object-Relational Mapping) e interagir com o banco de dados usando Python em vez de SQL puro.

---

### 🔹 Flask-Login
Extensão para gerenciamento de autenticação de usuários. Facilita login, logout, sessão de usuários e proteção de rotas.

---

### 🔹 Werkzeug
Toolkit WSGI que serve de base para o Flask. Gerencia requisições, respostas, roteamento, tratamento de erros e inclui um debugger web interativo.

---

### 🔹 psycopg2-binary
Driver PostgreSQL para Python. Usado pelo SQLAlchemy para conectar e interagir com bancos PostgreSQL.

---

### 🔹 python-dotenv
Permite carregar variáveis de ambiente a partir de um arquivo `.env`. Útil para gerenciar configurações sensíveis como chaves secretas e strings de conexão.

---

### 🔹 bcrypt
Biblioteca para hashing de senhas. Usada para armazenar senhas de forma segura (com sal e algoritmo de criptografia resistente a ataques de força bruta).

---

