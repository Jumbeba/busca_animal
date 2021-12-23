from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(r'C:\Users\RAFAEL\Documents\GitHub\busca_animal\chromedriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        '''
        Teste se um usuário encontra um animal na pesquisa
        '''
        # Vini deseja encontrar um novo animal para adotar.


        # Ele encontra o “Busca Animal” e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')

        # porque vê no menu do site escrito “Busca Animal”.
        #sugestão do pycharm: brand_element = self.browser.find_elements_by('.navbar')
        brand_element = self.browser.find_elements_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome, então vai digitar ali, em algum lugar vai ter um campo onde ele vai digitar o nome do animal que vai exibir


        # Ele digita, ele pesquisar, leão, e clica no botão pesquisar.


        # Ele desiste de adotar um leão

        pass

