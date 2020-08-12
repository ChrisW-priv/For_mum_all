def make_xml_from_xlsx(original_file='*.xlsx', form='', sheet_name='Arkusz1'):
    import xml.etree.ElementTree as ET
    import pandas as pd
    import datetime

    df = pd.read_excel(original_file, sheet_name=sheet_name)
   
    package_setup = {'xmlns': 'http://ps.stat.gov.pl/ps/schema/sprawozdanie',
                     'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
                     'xsi:schemaLocation': "http://ps.stat.gov.pl/ps/schema/sprawozdanie sprawozdanie.xsd",
                     'formularzSymbol':str(df.at[0,'formularzSymbol']),
                     'formularzWersja':str(df.at[0,'formularzWersja']),
                     'numerSprawozdania':str(df.at[0,'numerSprawozdania'])
    }

    package = ET.Element('Sprawozdanie')
    elements = ET.SubElement(package, 'Elementy')
    
    for key, value in package_setup.items():
        package.set(key, value)

    df = df.drop(columns=['formularzSymbol', 'formularzWersja', 'numerSprawozdania'])
    
    additional_cols = ['iloscSekcji', 'id2', 'id3', 'widoczna']
    for col in additional_cols:
        try:
            df = df.drop(columns=col)
        except Exception:
            continue

    for row in range(len(df)):
        field = ET.SubElement(elements, 'Pole')

        for column in df.columns:
            if str(df.at[row, column]) == 'nan':
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


    new_file = f"E:/New_XML_{form}_202007.xml"
    myfile = open(new_file, "wb")
    mydata = ET.tostring(package)
    myfile.write(mydata)


if __name__ == '__main__':
    make_xml_from_xlsx("E:/DG-1.xlsx", 'DG-1')