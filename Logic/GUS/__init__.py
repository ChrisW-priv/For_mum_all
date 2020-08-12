from selenium import webdriver
from contextlib import contextmanager
from time import sleep
import pandas as pd


class GUSAutomated:
    def __init__(self, user_id='', pwd='', phone='', email='', name=''):
        self.name = name
        self.phone = phone
        self.email = email
        self.driver = webdriver.Chrome("Logic/chromedriver.exe")
        
        self.driver.get("https://urldefense.proofpoint.com/v2/url?u=https-3A__raport.stat.gov.pl"
                        "&d=DwIFBA&c=vB1XvbdVorFiBi73ukS05g&r=8pFXRQZHfARhT2wBLn_ZEFVB2T7jg7VK4xvHRIdDtzY"
                        "&m=OgkJoVqga3m_B5IThx8iwBgxNRoPShcJYvCe6lkvmmc"
                        "&s=MKVnYgX0aZEg5fHt_TglCYaKzIoCioJRvmHZmb5IQFY"
                        "&e=")

        self.driver.find_element_by_xpath("//button[contains(text(), 'Zamknij')]")\
            .click()

        with self.wait_for_page_load(timeout=10):
            self.driver.find_element_by_xpath("//input[@name=\"j_username\"]") \
                .send_keys(user_id)
            self.driver.find_element_by_xpath("//input[@name=\"j_password\"]") \
                .send_keys(pwd)
            self.driver.find_element_by_xpath('//a[@class="input_button"]') \
                .click()

        self.driver.find_element_by_xpath('//a[@title="Przejdź"]') \
            .click()
        
        sleep(3)

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support.expected_conditions import staleness_of

        try:
            old_page = self.driver.find_element_by_tag_name('html')
            yield
            WebDriverWait(self.driver, timeout).until(
                staleness_of(old_page))
        except TimeoutError:
            print('Page took to long to load')
        except Exception:
            pass

    def choose_form(self, form=''):
        self.driver.find_elements_by_xpath('//a[@class="autofilter"]')[1] \
            .click()
        self.driver.find_element_by_xpath("//input[@id=\"formSymbol\"]") \
            .send_keys(form)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="listaBadanAutoFilter"]/fieldset[2]/div/a[1]') \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('//a[@title="Formularz"]') \
            .click()
        sleep(1)
        # switch to widow with form to fill
        with self.wait_for_page_load():
            self.driver.switch_to.window(self.driver.window_handles[1])

    def send_contact_info(self, xpath, info):
        cell = self.driver.find_element_by_xpath(xpath)
        cell.clear()
        cell.send_keys(info)

    def send_value_to_form(self, cell_id, value, page):
        print(cell_id, value, page)
        try:
            cell = self.driver.find_element_by_xpath(f"//input[@id='{cell_id}']")
            cell.clear()
            cell.send_keys(str(int(value)))
            sleep(0.1)
        except Exception as e:
            print('Exeption!:', e)

    def set_correct_form_page_in_sp_form(self, form_nr=''):
        self.driver.find_element_by_xpath(f'//select[@id="strony"]/option[contains(text(), "{form_nr}.")]').click()

    from ._f01 import f01
    from ._sp import sp
    from ._dg1 import dg1
    from ._c01 import c01
    from ._rf01 import rf01
