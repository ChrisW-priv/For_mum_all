import os

def xml_from_xlsx_GUS(original_file='*.xlsx', form='', sheet_name='Arkusz1'):
    from datatime import datetime
    import xml.etree.ElementTree as ET
    import pandas as pd

    df = pd.read_excel(original_file, sheet_name=sheet_name)
   
    package_setup = {'xmlns': 'http://ps.stat.gov.pl/ps/schema/sprawozdanie',
                     'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
                     'xsi:schemaLocation': "http://ps.stat.gov.pl/ps/schema/sprawozdanie sprawozdanie.xsd",
                     'formularzSymbol':str(df.at[0,'formularzSymbol']),
                     'formularzWersja':str(df.at[0,'formularzWersja']),
                     'numerSprawozdania':str(df.at[0,'numerSprawozdania'])
    }
    package = ET.Element('Sprawozdanie')
    for key, value in package_setup.items():
        package.set(key, value)
    df = df.drop(columns=['formularzSymbol', 'formularzWersja', 'numerSprawozdania'])

    elements = ET.SubElement(package, 'Elementy')
    
    columns_to_be_ignored = ['iloscSekcji', 'id2', 'id3', 'widoczna']
    for row in range(len(df)):
        field = ET.SubElement(elements, 'Pole')

        for column in df.columns:
            if str(df.at[row, column]) == 'nan' or column in columns_to_be_ignored:
                continue
            else:
                field.set(column, str(df.at[row, column]))
    
    if form == 'DG-1':
        end =  ET.SubElement(elements, 'Sekcja')
        end.set('id','n_dane_sprawozdawcy')
        end.set('widoczna','false')
    elif form == 'C-01':
        end =  ET.SubElement(elements, 'MultiSekcja')
        end.set('id','sek0')
        end.set('ilośćSekcji','4')

        end =  ET.SubElement(elements, 'Sekcja')
        end.set('id','sek0')
        end.set('widoczna','false')
    elif form == 'DNU-K':
        pass

    new_file = os.path.join(path_to_folder, f"{form}_{datetime.now().strftime('%m_%Y')}.xml")
    mydata = ET.tostring(package)
    with open(new_file, "wb") as myfile:
        myfile.write(mydata)


if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.expanduser("~/Desktop"), 'New'), exist_ok=True)
    xml_from_xlsx_GUS(os.path.expanduser("~/Desktop/NEW"), "E:/DG-1.xlsx", 'DG-1')
