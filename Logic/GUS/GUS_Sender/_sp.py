def sp(self, filename_or_file_path='SP.xlsx'):
    # contact info
    self.send_contact_info('//input[@id="email"]', self.email)
    self.send_contact_info('//input[@id="tl1"]', self.phone)
    self.send_contact_info('//input[@id="emailos"]', self.email)
    self.send_contact_info('//input[@id="telefon"]', self.phone)

    # main body:
    # wb = xl.load_workbook(filename_or_file_path)
    wb = pd.read_excel(filename_or_file_path)
    sheetnames = [key for key,item in wb.items()]

    for sheet_name in sheetnames:
        from pandas import DataFrame

        df = pd.read_excel(filename_or_file_path, sheet_name=sheet_name)

        if int(sheet_name) in range(7, 8 + 1):
            self.set_correct_form_page_in_sp_form(sheet_name)

            # first col on site
            col_name_for_id = 'first_col_id_nr'
            col_name_for_value = 'first_value'
            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]
                col_number = 1

                cell_id = f'ba{nr}r{col_number}'

                self.send_value_to_form(cell_id, value, sheet_name)

            # second col on site
            col_name_for_value = 'second_value'
            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]
                col_number = 2

                cell_id = f'ba{nr}r{col_number}'

                self.send_value_to_form(cell_id, value, sheet_name)

        if int(sheet_name) in range(9, 10 + 1):
            self.set_correct_form_page_in_sp_form(sheet_name)

            # first col on site
            col_name_for_id = 'first_col_id_nr'
            col_name_for_value = 'first_value'
            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]
                col_number = 1

                cell_id = f'bp{nr}r{col_number}'

                self.send_value_to_form(cell_id, value, sheet_name)

            # second col on site
            col_name_for_value = 'second_value'
            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]
                col_number = 2

                cell_id = f'bp{nr}r{col_number}'

                self.send_value_to_form(cell_id, value, sheet_name)

        if sheet_name == '11':
            self.set_correct_form_page_in_sp_form(sheet_name)

            # first col on site
            col_name_for_id = 'first_col_id_nr'
            col_name_for_value = 'first_value'
            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]
                col_number = 1

                cell_id = f'bu{nr}r{col_number}'

                self.send_value_to_form(cell_id, value, sheet_name)

            # second col on site
            col_name_for_value = 'second_value'
            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]
                col_number = 2

                cell_id = f'bu{nr}r{col_number}'

                self.send_value_to_form(cell_id, value, sheet_name)

        if int(sheet_name) in range(12, 15+1):
            self.set_correct_form_page_in_sp_form(sheet_name)

            col_name_for_id = 'id_nr'
            col_name_for_value = 'value'

            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]

                cell_id = f'rs{nr}'

                self.send_value_to_form(cell_id, value, sheet_name)

        if sheet_name == '16':
            self.set_correct_form_page_in_sp_form(sheet_name)

            col_name_for_id = 'id_nr'
            col_name_for_value = 'value'

            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]

                cell_id = f'rsun{nr}'

                self.send_value_to_form(cell_id, value, sheet_name)

        if sheet_name == '17':
            self.set_correct_form_page_in_sp_form(sheet_name)

            for row_index in range(df.shape[0]):
                row = df.loc[row_index]
                for col, value in enumerate(row[1:]):
                    nr = row_index*8+col

                    cell_id = f'rsn{nr}'

                    self.send_value_to_form(cell_id, value, sheet_name)

        if sheet_name == '18':
            self.set_correct_form_page_in_sp_form(sheet_name)

            col_name_for_id = 'id_nr'
            col_name_for_value = 'value'

            for row_index in range(df.shape[0]):
                row = df.loc[row_index]

                nr = row[col_name_for_id]
                value = row[col_name_for_value]

                cell_id = f'stn1{nr}'

                self.send_value_to_form(cell_id, value, sheet_name)

        if sheet_name == '19':
            self.set_correct_form_page_in_sp_form(sheet_name)

            # first table
            d = DataFrame()
            df1 = [df[column] for column in df.columns if column.__contains__('1.')]
            for c in df1:
                d = pd.concat([d, c], axis=1)

            for row in range(2+1):
                for column_name in d.columns[1:]:
                    cell_value = d.at[row, column_name]
                    nr = (str(row * 8 + int(column_name[-1])).zfill(2))
                    cell_id = f'oa{nr}'

                    self.send_value_to_form(cell_id=cell_id, value=cell_value, page=sheet_name)

            # second table
            d = DataFrame()
            df2 = [df[column] for column in df.columns if column.__contains__('2.')]
            for c in df2:
                d = pd.concat([d, c], axis=1)

            for row in range(1+1):
                for column_name in d.columns[1:]:
                    cell_value = d.at[row, column_name]
                    nr = str(row * 8 + int(column_name[-1]))
                    cell_id = f'lf{nr}'

                    self.send_value_to_form(cell_id=cell_id, value=cell_value, page=sheet_name)

            # third table
            d = DataFrame()
            df3 = [df[column] for column in df.columns if column.__contains__('3.')]
            for c in df3:
                d = pd.concat([d, c], axis=1)

            for row in range(2 + 1):
                for column_name in d.columns[1:]:
                    cell_value = d.at[row, column_name]
                    nr = (str(row * 8 + int(column_name[-1])).zfill(2))
                    cell_id = f'fn{nr}'

                    self.send_value_to_form(cell_id=cell_id, value=cell_value, page=sheet_name)

        if sheet_name == '26':
            self.set_correct_form_page_in_sp_form(sheet_name)

            # first column of first table:
            col_name_for_value = '1.01'

            for row_index in range(4+1):
                value = df.at[row_index, col_name_for_value]

                cell_id = f'do{row_index}'

                self.send_value_to_form(cell_id, value, sheet_name)

            # second column of first table:
            col_name_for_value = '1.02'

            for row_index in range(4+1):
                value = df.at[row_index, col_name_for_value]

                cell_id = f'zak{row_index}'

                self.send_value_to_form(cell_id, value, sheet_name)

            # first column of second table:
            col_name_for_value = '2.01'

            for row_index in range(5+1):
                value = df.at[row_index, col_name_for_value]

                cell_id = f'pp{row_index}'

                self.send_value_to_form(cell_id, value, sheet_name)

        if sheet_name == '30':
            self.set_correct_form_page_in_sp_form(sheet_name)

            for column_index in range(2):
                column_index += 1
                for row_index in range(5+1):
                    value = df.at[row_index, column_index]

                    cell_id = f'd2p11_0{row_index}{column_index}'

                    self.send_value_to_form(cell_id, value, sheet_name)

        if sheet_name == '31':
            # First table
            column_name = 'First column'
            for row_index in range(1+1):
                cell_id = f'd2p14{row_index}'
                value = df.at[row_index, column_name]
                self.send_value_to_form(cell_id, value, sheet_name)

            # Second table
            column_name = 'Second column'
            for row_index in range(1 + 1):
                cell_id = f'd2p15{row_index}'
                value = df.at[row_index, column_name]
                self.send_value_to_form(cell_id, value, sheet_name)
