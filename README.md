# E-commerce Back-end

Este projeto implementa um sistema de e-commerce utilizando FastAPI como framework backend e MongoDB como banco de dados.

Funcionalidades principais:

- CRUD de usuários (criação, atualização e exclusão de contas)
- CRUD de produtos
- Carrinho de compras por usuário
- Simulação de pagamento (confirmação de pedido)

## Execução

### Ambiente Virtual Python

Criação, execução e instalação de dependências Python:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Criação do Banco de Dados

Criação de um banco de dados utilizando MongoDB:
```
mongosh < create_database.js
```


### Ativação do Sistema

Execução na raiz do projeto:
```
uvicorn main:app --reload
```