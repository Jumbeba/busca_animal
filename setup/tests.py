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


        # Ele encontra o “Busca Animal” e decide pesquisar no site,
        home_page = self.browser.get(self.live_server_url + '/')

        # porque vê no menu do site escrito “Busca Animal”.
        # noinspection PyDeprecation
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome, então vai digitar ali, em algum lugar vai ter um campo onde ele vai digitar o nome do animal que vai exibir
        # noinspection PyDeprecation
        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo : Leão, Urso...')

        # Ele digita, ele pesquisar, leão, e clica no botão pesquisar.
        buscar_animal_input.send_keys('leão')
        self.browser.find_element_by_css_selector('form button').click()

        # O site exibe 4 caracteristicas do animal pesquisado
        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)

        # Ele desiste de adotar um leão


