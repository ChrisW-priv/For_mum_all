def wb_form_gd1():
    wb = Workbook()

    for i in range(2, 3+1):
        wb.create_sheet(title=str(i))

    ws = wb['2']
    ws.cell(1, 1, value='first_col_id_nr')
    ws.cell(1, 2, value='first_value')
    ws.cell(1, 3, value='second_value')

    ws = wb['3']
    ws.cell(1, 1, value='first_col_id_nr')
    ws.cell(1, 2, value='first_value')
    ws.cell(1, 3, value='second_value')

    filename = 'GD-1.xlsx'
    wb.save(filename)
