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
    table_html = df.to_html(classes='data', header="true", index=False)
    return render_template('table.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)