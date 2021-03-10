from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://127.0.0.1:8000/")

        # Verifica o título do site
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")

        # Digita "Buy peacock feathers" em uma caixa de texto

        # Quando pressiona enter, a página é atualizada, e agora a página
        # lista: "1: Buy peacock feathers" como um item em uma lista de tarefas

        # Insere/digita "Use peacock feathers to make a fly"

        # A página é atualizada novamente e agora mostra os dois itens na lista

        # Verifica se o site irá lembrar da lista
        # E verifica se o site gerou um URL único


if __name__ == '__main__':
    unittest.main()
