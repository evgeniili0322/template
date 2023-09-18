import allure

from selene import browser, have


class MainPage:
    @allure.step('Open main page')
    def open(self):
        browser.open('')

    @allure.step('Assert banner text')
    def assert_banner_text(self):
        browser.element('[field="tn_text_1679499443035"]').should(have.exact_text('Создаём инфраструктурные сетевые '
                                                                                  'решения для крупного бизнеса в '
                                                                                  'сфере страхования логистики и '
                                                                                  'медицины, специализируемся на '
                                                                                  'работе со сложными технологиями, '
                                                                                  'в том числе блокчейн и нейронные '
                                                                                  'сети.'))

    @allure.step('Assert info text')
    def assert_info_text(self):
        browser.all('#rec571160648 .tn-atom').odd.should(have.exact_texts(
            'Нами создана крупнейшая транзакционная сеть на блокчейне в России — более 100 транзакций в секунду',
            'Мы — ИТ-компания, аккредитованная Минцифры России',
            'С июля 2018 г. — резидент особой экономической зоны в Калининградской области',
            'Решения компании зарегистрированы в реестре отечественного ПО'
        ))

    @allure.step('Assert partners text')
    def assert_partners_text(self):
        browser.all('#rec571157876 [data-elem-type="text"]').should(have.exact_texts(
            'Партнёры',
            'С нами работают 8 из 15 крупнейших страховых компаний России'
        ))
