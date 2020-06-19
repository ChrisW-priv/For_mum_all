def wb_form_f01():
    wb = Workbook()

    for i in range(3, 12+1):
        wb.create_sheet(title=str(i))

    def create_content():
        for i in range(3, 7+1):
            ws = wb[str(i)]
            ws.cell(1, 1, value='id_nr')
            ws.cell(1, 2, value='value')

        ws = wb['8']
        ws.cell(1, 1, value='first_col_id_nr')
        ws.cell(1, 2, value='first_value')
        ws.cell(1, 3, value='second_value')

        ws = wb['9']
        ws.cell(1, 1, value='id_nr')
        ws.cell(1, 2, value='value')

        ws = wb['10']
        ws.cell(1, 1, value='id_nr')
        ws.cell(1, 2, value='value')
        ws.cell(2, 1, value='r1')
        ws.cell(3, 1, value='r2')
        ws.cell(4, 1, value='r3')
        ws.cell(5, 1, value='r3')
        ws.cell(2, 3, value='(01 left)')
        ws.cell(3, 3, value='(02 left)')
        ws.cell(4, 3, value='(03 right)')
        ws.cell(5, 3, value='(04 right)')

        ws = wb['11']
        ws.cell(1, 1, value='first_col_id_nr')
        ws.cell(1, 2, value='first_value')
        ws.cell(1, 3, value='second_value')
        ws.cell(1, 4, value='third_value')

        ws = wb['12']
        ws.cell(1, 1, value='first_tabel_id_nr')
        ws.cell(1, 2, value='first_tabel_value')
        ws.cell(1, 3, value='second_tabel_id_nr')
        ws.cell(1, 4, value='second_tabel_value')
        ws.cell(2, 1, value='1')
        ws.cell(3, 1, value='2')
        ws.cell(4, 1, value='3')
        ws.cell(5, 1, value='4')
        ws.cell(2, 3, value='5')
        ws.cell(3, 3, value='6')
        ws.cell(4, 3, value='7')
        ws.cell(5, 3, value='8')

    create_content()

    filename = 'F-01.xlsx'
    wb.save(filename)
