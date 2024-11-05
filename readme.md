# Teste de Aplicação Flask - Tabela de Alunos

Este projeto é uma aplicação simples desenvolvida em Flask que exibe uma tabela com as notas de alunos. Ele serve como um exemplo básico de como utilizar Flask para renderizar dados em uma tabela HTML a partir de um DataFrame do Pandas.

## Funcionalidades

- **Página Inicial**: Uma interface de boas-vindas com um link para acessar a tabela de alunos.
- **Tabela de Alunos**: Exibe o nome dos alunos e suas respectivas notas em uma tabela bem formatada.

## Pré-requisitos

- Python 3.x
- Flask
- Pandas

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL do seu repositório>
   cd teste_git_python

2.Crie e ative um ambiente virtual:

    python -m venv venv
    
    'source venv/bin/activate
    
    # No Windows, `venv\Scripts\activate`

3.Instale as dependências:
    pip install flask pandas

Executando a Aplicação
Para executar a aplicação, utilize o seguinte comando:

python app.py

A aplicação estará disponível em http://127.0.0.1:5000.

Executando Testes
Para executar os testes automatizados, utilize:

python -m unittest discover tests
