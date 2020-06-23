def sort(file, list_):
    import pandas as pd
    df = pd.read_excel(file, sheet_name='Arkusz1')
    df.sort_values(by=list_, inplace=True)
    df.reset_index(drop=True, inplace=True)
    for row in range(df['nrWiersza'].count()):
        df.loc[row, 'nrWiersza'] = row + 1

    df.to_excel(file, index=False, sheet_name='Arkusz1')
