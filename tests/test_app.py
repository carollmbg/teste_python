import unittest
from app import app  # Importa a aplicação Flask para testes

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        #método executado antes de cada teste. Cria um cliente de teste que permite fazer requisições HTTP para a aplicação sem a necessidade de um servidor real.
    
        self.app = app.test_client()  # Cria um cliente de teste
        self.app.testing = True  # Habilita o modo de testes para capturar exceções

    def test_index(self):
        #Testa a página inicial ('/'). Verifica se o status da resposta.
        
        response = self.app.get('/')  

        # Verifica se o status da resposta é 200
        self.assertEqual(response.status_code, 200, "Erro: Status code não é 200!")
        
        # Verifica se o conteúdo esperado está presente na resposta
        self.assertIn(b'Welcome to the Index Page', response.data, "Erro: Conteúdo não encontrado na página!")

    def test_table(self):
        #Testa a página da tabela e verifica se o status da resposta é 200 (OK) 
        response = self.app.get('/table')  # Faz uma requisição GET para a rota '/table'
        
        # Verifica se o status da resposta é 200
        self.assertEqual(response.status_code, 200, "Erro: Status code não é 200!")
        
        # Verifica se o conteúdo esperado está presente na resposta
        self.assertIn(b'Tabela de Alunos e Notas', response.data, "Erro: Conteúdo da tabela não encontrado na página!")

if __name__ == '__main__':
    unittest.main()  # Executa os testes