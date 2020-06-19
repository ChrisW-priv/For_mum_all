def rf01(self, filename_or_file_path='RF-01.xlsx'):
    self.send_contact_info('//input[@name="email1"]', self.email)
    self.send_contact_info('//input[@name="email2"]', self.email)
    self.send_contact_info('//input[@name="tel0"]', self.phone[:2])
    self.send_contact_info('//input[@name="tel"]', self.phone[2:])
    self.driver.find_element_by_xpath('//input[@id="3fp"]').click()

    # done
    self.driver.find_element_by_xpath('//a[@id="nextPage"]') \
        .click()
    sleep(1)

    # main body:
    # wb = xl.load_workbook(filename_or_file_path)
    wb = pd.read_excel(filename_or_file_path)
    sheetnames = [key for key,item in wb.items()]

    for sheet_name in sheetnames:
        df = pd.read_excel(filename_or_file_path, sheet_name=sheet_name)

        sleep(1)
        try:
            if int(sheet_name) in range(2, 3+1):
                col_name_for_id = 'id_nr'
                col_name_for_value = 'value'

                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id])
                    value = row[col_name_for_value]

                    cell_id = f'a{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)
        except ValueError:
            print('sheet_name no good')
            continue

        try:
            if sheet_name == '4':
                col_name_for_id = 'id_nr'
                col_name_for_value = 'value'

                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id])
                    value = row[col_name_for_value]

                    cell_id = f'p{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)
        except ValueError:
            print('sheet_name no good')
            continue

        # done with one page
        self.driver.find_element_by_xpath('//a[@id="nextPage"]') \
            .click()
        sleep(1)
