def dg1(self, filename_or_file_path='DG-1.xlsx'):
    self.send_contact_info('//input[id="n_daneOsob"]', self.name)
    self.send_contact_info('//input[id="n_email_sprawozdawca"]', self.email)
    self.send_contact_info('//input[id="n_telefon"]', self.phone)

    ids_of_second_page_table = {
        'st1': 'Sw_1b',
        'st2': 'Sb_1b',
        'st3': 'Si_1b',
        'st4': 'Sz_1b',
        'st5': 'Sh_1b',
        'st6': 'Pp_1b',
        'st7': 'Pz_1b',
        'st8': None,
        'st9': 'Wb_1b',
        'st10': 'Wz_1b',
        'st11': None,
        'st12': 'Sd_1b',
        'st13': 'St_1b',
        'st14': 'Sr_1b',
        'st15': 'Da_1b',
        'st16': 'Dt_1b',
        'st17': 'Dp_1b',
        'st18': 'Ia_5b',
        'nd1': 'Sw_2b',
        'nd2': 'Sb_2b',
        'nd3': 'Si_2b',
        'nd4': 'Sz_2b',
        'nd5': 'Sh_2b',
        'nd6': None,
        'nd7': 'Pz_2b',
        'nd8': 'Cp_2b',
        'nd9': 'Wb_2b',
        'nd10': 'Wz_2b',
        'nd11': 'Ws_2b',
        'nd12': 'Sd_2b',
        'nd13': 'St_2b',
        'nd14': 'Sr_2b',
        'nd15': 'Da_2b',
        'nd16': 'Dt_2b',
        'nd17': 'Dp_2b',
        'nd18': None,
    }
    ids_of_third_page_table = {
        'st1': 'Ew_1b',
        'st2': 'Ews-1b',
        'st3': 'Eh-1b',
        'st4': 'Ehs-1b',
        'st5': 'Nz-1b',
        'st6': 'Ne-1b',
        'st7': 'Nes-1b',
        'nd1': 'Ew_2b',
        'nd2': 'Ews-2b',
        'nd3': 'Eh-2b',
        'nd4': 'Ehs-2b',
        'nd5': None,
        'nd6': None,
        'nd7': None,
    }

    # main body:
    # wb = xl.load_workbook(filename_or_file_path)
    wb = pd.read_excel(filename_or_file_path)
    sheetnames = [key for key,item in wb.items()]

    for sheet_name in sheetnames:
        df = pd.read_excel(filename_or_file_path, sheet_name=sheet_name)

        sleep(1)
        try:
            if int(sheet_name) in range(2, 3+1):
                # first col on site
                col_name_for_id = 'first_col_id_nr'
                col_name_for_value = 'first_value'

                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]
                    value = row[col_name_for_value]
                    cell_id = ids_of_second_page_table[f'st{col_name_for_id}']

                    self.send_value_to_form(cell_id, value, sheet_name)

                # second col on site
                col_name_for_value = 'second_value'
                for row_index in range(df.shape[0]):
                    row = df.loc[row_index]

                    value = row[col_name_for_value]

                    cell_id = ids_of_third_page_table[f'nd{col_name_for_id}']

                    self.send_value_to_form(cell_id, value, sheet_name)
        except Exception as e:
            print(e)
            continue
