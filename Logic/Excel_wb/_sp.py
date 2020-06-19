def wb_form_sp():
    wb = Workbook()

    for i in range(7, 19+1):
        wb.create_sheet(title=str(i))
    add_ = ['26', '30', '31']
    for i in add_:
        wb.create_sheet(title=str(i))

    def create_content():
        for i in range(7, 11+1):
            ws = wb[str(i)]
            ws.cell(1, 1, value='first_col_id_nr')
            ws.cell(1, 2, value='first_value')
            ws.cell(1, 3, value='second_value')

        for i in range(12, 16+1):
            ws = wb[str(i)]
            ws.cell(1, 1, value='id_nr')
            ws.cell(1, 2, value='value')

        ws = wb['17']
        ws.cell(1, 1, value='0')
        ws.cell(1, 2, value='1')
        ws.cell(1, 3, value='2')
        ws.cell(1, 4, value='3')
        ws.cell(1, 5, value='4')
        ws.cell(1, 6, value='5')
        ws.cell(1, 7, value='6')
        ws.cell(1, 8, value='7')
        ws.cell(1, 9, value='8')
        ws.cell(2, 1, value='01')
        ws.cell(3, 1, value='02')
        ws.cell(4, 1, value='03')
        ws.cell(5, 1, value='04')
        ws.cell(6, 1, value='05')
        ws.cell(7, 1, value='06')
        ws.cell(8, 1, value='07')
        ws.cell(9, 1, value='08')
        ws.cell(10, 1, value='09')
        ws.cell(11, 1, value='10')
        ws.cell(12, 1, value='11')
        ws.cell(13, 1, value='12')

        ws = wb['18']
        ws.cell(1, 1, value='id_nr')
        ws.cell(1, 2, value='value')

        ws = wb['19']
        ws.cell(1, 1, value='1.00')
        ws.cell(1, 2, value='1.01')
        ws.cell(1, 3, value='1.02')
        ws.cell(1, 4, value='1.03')
        ws.cell(1, 5, value='1.04')
        ws.cell(1, 6, value='1.05')
        ws.cell(1, 7, value='1.06')
        ws.cell(1, 8, value='1.07')
        ws.cell(1, 9, value='1.08')
        ws.cell(2, 1, value='1')
        ws.cell(3, 1, value='2')
        ws.cell(4, 1, value='3')

        ws.cell(1, 10, value='-')
        ws.cell(2, 10, value='-')
        ws.cell(3, 10, value='-')
        ws.cell(4, 10, value='-')
        ws.cell(5, 10, value='-')
        ws.cell(6, 10, value='-')
        ws.cell(7, 10, value='-')

        ws.cell(1, 11, value='2.00')
        ws.cell(1, 12, value='2.01')
        ws.cell(1, 13, value='2.02')
        ws.cell(1, 14, value='2.03')
        ws.cell(1, 15, value='2.04')
        ws.cell(2, 11, value='1')
        ws.cell(3, 11, value='2')

        ws.cell(1, 16, value='-')
        ws.cell(2, 16, value='-')
        ws.cell(3, 16, value='-')
        ws.cell(4, 16, value='-')
        ws.cell(5, 16, value='-')
        ws.cell(6, 16, value='-')
        ws.cell(7, 16, value='-')

        ws.cell(1, 17, value='3.00')
        ws.cell(1, 18, value='3.01')
        ws.cell(1, 19, value='3.02')
        ws.cell(1, 20, value='3.03')
        ws.cell(1, 21, value='3.04')
        ws.cell(1, 22, value='3.05')
        ws.cell(1, 23, value='3.06')
        ws.cell(1, 24, value='3.07')
        ws.cell(1, 25, value='3.08')
        ws.cell(1, 26, value='3.09')
        ws.cell(2, 17, value='1')
        ws.cell(3, 17, value='2')
        ws.cell(4, 17, value='3')
        ws.cell(5, 17, value='4')
        ws.cell(6, 17, value='5')
        ws.cell(7, 17, value='6')

        ws = wb['26']
        ws.cell(1, 1, value='1.00')
        ws.cell(1, 2, value='1.01')
        ws.cell(1, 3, value='1.02')
        ws.cell(2, 1, value='1')
        ws.cell(3, 1, value='2')
        ws.cell(4, 1, value='3')
        ws.cell(5, 1, value='4')
        ws.cell(6, 1, value='5')

        ws.cell(1, 4, value='-')
        ws.cell(2, 4, value='-')
        ws.cell(3, 4, value='-')
        ws.cell(4, 4, value='-')
        ws.cell(5, 4, value='-')
        ws.cell(6, 4, value='-')
        ws.cell(7, 4, value='-')

        ws.cell(1, 5, value='2.00')
        ws.cell(1, 6, value='2.01')
        ws.cell(2, 5, value='1')
        ws.cell(3, 5, value='2')
        ws.cell(4, 5, value='3')
        ws.cell(5, 5, value='4')
        ws.cell(6, 5, value='5')
        ws.cell(7, 5, value='6')

        ws = wb['30']
        ws.cell(1, 1, value='0')
        ws.cell(1, 2, value='1')
        ws.cell(1, 3, value='2')
        ws.cell(2, 1, value='01')
        ws.cell(3, 1, value='02')
        ws.cell(4, 1, value='03')
        ws.cell(5, 1, value='04')
        ws.cell(6, 1, value='05')
        ws.cell(7, 1, value='06')

        ws = wb['31']
        ws.cell(1, 1, value='ID')
        ws.cell(1, 2, value='First column')
        ws.cell(1, 3, value='Second column')
        ws.cell(2, 1, value='01')
        ws.cell(3, 1, value='02')

    create_content()

    filename = 'SP.xlsx'
    wb.save(filename)
