def f01(self, filename_or_file_path='F-01.xlsx'):
        # page 1
        #self.send_contact_info('//input[@name="e_mail"]', self.email)
        #sleep(1)
        #self.send_contact_info('//input[@name="tel"]', self.phone)
        #sleep(1)
        #self.send_contact_info('//input[@name="e_mail_o"]', self.email)
        sleep(1)

        # done
        self.driver.find_element_by_xpath('//a[@id="nextPage"]') \
            .click()
        sleep(1)
        # page 2
        sleep(1)
        # done
        self.driver.find_element_by_xpath('//a[@id="nextPage"]') \
            .click()
        sleep(1)

        # main body:
        wb = pd.read_excel(filename_or_file_path)
        sheetnames = [key for key,item in wb.items()]

        for sheet_name in sheetnames:
            df = pd.read_excel(filename_or_file_path, sheet_name=sheet_name)

            sleep(1)
            try:
                if int(sheet_name) in range(3, 7+1):
                    col_name_for_id = 'id_nr'
                    col_name_for_value = 'value'

                    for row_index in range(df.shape[0]):
                        row = df.loc[row_index]

                        nr = str(int(row[col_name_for_id])).zfill(2)
                        value = row[col_name_for_value]

                        cell_id = f'd1w{nr}'

                        self.send_value_to_form(cell_id, value, sheet_name)

            except ValueError:
                print('sheet_name no good')
                continue

            if sheet_name == '8':

                # first col on site
                col_name_for_id = 'first_col_id_nr'
                col_name_for_value = 'first_value'
                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id]).zfill(2)
                    value = row[col_name_for_value]
                    col_number = 1

                    cell_id = f'd2w{nr}r{col_number}'

                    self.send_value_to_form(cell_id, value, sheet_name)

                # second col on site
                col_name_for_value = 'second_value'
                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id]).zfill(2)
                    value = row[col_name_for_value]
                    col_number = 2

                    cell_id = f'd2w{nr}r{col_number}'

                    self.send_value_to_form(cell_id, value, sheet_name)

            if sheet_name == '9':
                col_name_for_id = 'id_nr'
                col_name_for_value = 'value'

                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id]).zfill(2)
                    value = row[col_name_for_value]

                    cell_id = f'd3w{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)

            if sheet_name == '10':
                # id must have 'r{nr}' format or it will not work
                col_name_for_id = 'id_nr'
                col_name_for_value = 'value'

                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id]).zfill(2)
                    value = row[col_name_for_value]

                    cell_id = f'{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)

            if sheet_name == '11':

                # first column on page, id = r1w{nr}
                col_name_for_id = 'first_col_id_nr'
                col_name_for_value = 'first_value'
                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id]).zfill(2)
                    value = row[col_name_for_value]

                    cell_id = f'r1w{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)

                # second column on page, id = r2w{nr}
                col_name_for_value = 'second_value'
                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id]).zfill(2)
                    value = row[col_name_for_value]

                    cell_id = f'r2w{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)

                # third column on page, id = r3w{nr}
                col_name_for_value = 'third_value'
                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = str(row[col_name_for_id]).zfill(2)
                    value = row[col_name_for_value]

                    cell_id = f'r3w{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)

            if sheet_name == '12':

                # numbers from 1 to 4
                col_name_for_id = 'first_tabel_id_nr'
                col_name_for_value = 'first_tabel_value'
                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = (row[col_name_for_id])
                    value = row[col_name_for_value]

                    cell_id = f'd3r1w{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)

                # numbers from 5 to 8
                col_name_for_value = 'second_tabel_value'
                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    nr = (row[col_name_for_id])
                    value = row[col_name_for_value]

                    cell_id = f'd3r2w{int(nr) - 4}'

                    self.send_value_to_form(cell_id, value, sheet_name)

            # done with one page
            self.driver.find_element_by_xpath('//a[@id="nextPage"]') \
                .click()
            sleep(1)
