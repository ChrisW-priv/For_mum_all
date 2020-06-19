def c01(self, filename_or_file_path='C-01.xlsx'):
    self.send_contact_info('//input[id="n_imie"]', self.name.split(' ')[0])
    self.send_contact_info('//input[id="n_nazwisko"]', self.name.split(' ')[-1])
    self.send_contact_info('//input[id="n_telefon"]', self.phone)
    self.send_contact_info('//input[id="n_email_sprawozdawca"]', self.email)

    def choose_form(form=''):
        self.driver.find_element_by_xpath('//a[@class="autofilter"]') \
            .click()
        self.driver.find_element_by_xpath("//input[@id='filter_numer_rep'") \
            .send_keys(form)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="m1AutoFilter"]/fieldset[2]/div/a[1]') \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('//a[@title="Szczegóły wiersza"]') \
            .click()
        sleep(1)

    df = pd.read_excel(filename_or_file_path, sheet_name='Wartości_do_przepisania')

    for row in df.iterrows():
        form = str(int(row[1][0])).zfill(2)
        choose_form(form)
        for i, value in enumerate(row[1][1:]):
            self.send_value_to_form(cell_id=f'p{i + 1}b', value=value, page=form)
