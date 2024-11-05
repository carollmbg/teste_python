from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

##########################################################
########################### 01 ###########################
##########################################################
@app.route('/')
def index():
    return render_template('index.html')


##########################################################
########################### 02 ###########################
##########################################################
# CRIANDO O DATAFRAME
df = pd.DataFrame({
    'alunos': ['Renato', 'Fernando', 'Rodrigo', 'Ana', 'Joana', 'Silvio', 'Carolina'],
    'notas': [15.00, 39.58, 62.92, 41.46, 48.33, 63.13, 70.00]
})

# RENDERIZE OS VALORES DO DATAFRAME df EM UMA TABELA HTML DENTRO DA PÁGINA /table.html (CRIE UM HTML PARA ISSO)
@app.route('/table')
def table():
    # Converte o DataFrame em uma tabela HTML
    # O parâmetro 'classes' define a classe CSS para aplicar à tabela
    # O parâmetro 'header' define se o cabeçalho será mostrado (true)
    # O parâmetro 'index' define se o índice do DataFrame será exibido (false)
    table_html = df.to_html(classes='data', header="true", index=False)
    
    # Renderiza a página 'table.html' e passa a tabela gerada como parâmetro
    return render_template('table.html', table=table_html)

# Verifica se o script está sendo executado diretamente (não importado)
# Caso esteja, inicia o servidor da aplicação Flask no modo de desenvolvimento (debug=True)
if __name__ == '__main__':
    app.run(debug=True)