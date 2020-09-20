import os

def xml_from_xlsx_NBP(path_to_folder, original_file='*.xlsx', form='', sheet_name='Arkusz1'):
    from datatime import datetime
    import xml.etree.ElementTree as ET
    import pandas as pd

    df = pd.read_excel(original_file, sheet_name=sheet_name)
    for column_name in df.columns:
        if column_name.__contains__('ns0'):
            df.rename(columns={column_name: column_name.replace('ns0', 'prz')}, inplace=True)
        elif column_name.__contains__('ns2'):
            df.rename(columns={column_name: column_name.replace('ns2', 'ts')}, inplace=True)
        elif column_name.__contains__('ns3'):
            df.rename(columns={column_name: column_name.replace('ns3', 'td')}, inplace=True)

    package_setup = {'xmlns:prz': 'http://sprawozdawczosc.nbp.pl/schema/2019_02_01/przesylka',
                     'xmlns:ts': "http://sprawozdawczosc.nbp.pl/schema/wspolne/typySprawozdan",
                     'xmlns:td': "http://sprawozdawczosc.nbp.pl/schema/wspolne/typyDanych",
                     'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
                     'okres_sprawozdawczy': f"{df.at[0, 'okres_sprawozdawczy']}",
                     'xsi:schemaLocation': "http://sprawozdawczosc.nbp.pl/schema/2019_02_01/przesylka "
                                           "http://sprawozdawczosc.nbp.pl/schema/2019_02_01/przesylka.xsd"}
    package = ET.Element('prz:przesylka')
    for key in package_setup:
        content.set(key, package_setup[key])
    
    content_setup = {'dataWypelnienia': f"{str(df.at[0, 'dataWypelnienia']).split(' ')[0]}",
                     'xsi:type': f"ts:Spr{form}Type"}
    content = ET.SubElement(package, 'prz:sprawozdanie')
    for key in content_setup:
        content.set(key, content_setup[key])
    
    header_setup = {'td:regon': '63027533800000',
                    'ts:nazwa': 'Tarkett Polska Sp. z o.o.'}
    header = ET.SubElement(content, 'ts:naglowek')
    for key in header_setup:
        header_element = ET.SubElement(header, key)
        header_element.text = header_setup[key]    

    data = ET.SubElement(content, 'ts:dane')
    rows = ET.SubElement(data, 'ts:wiersze')

    for line in range(len(df)):
        try:
            index_num = str(int(df.at[line, 'nrWiersza']))
        except Exception as e:
            print(e)
            continue
        else:
            row = ET.SubElement(rows, 'ts:wiersz')
            row.set('nrWiersza', index_num)

            all_columns = df.drop(columns=['okres_sprawozdawczy',
                                           'dataWypelnienia', 'td:regon',
                                           'ts:nazwa', 'nrWiersza']).columns

            for key in all_columns:
                try:
                    elem = ET.SubElement(row, key)
                    elem.text = str(int(df.at[line, key]))
                except ValueError:
                    try:
                        elem = ET.SubElement(row, key)
                        elem.text = str(df.at[line, key])
                    except Exception as e:
                        print(e)
                        continue

    new_file = os.path.join(path_to_folder, f"{form}_{datetime.now().strftime('%m_%Y')}.xml")
    mydata = ET.tostring(package)
    with open(new_file, "wb") as myfile:
        myfile.write(mydata)

if __name__ == '__main__':
    os.makedirs(os.path.join(os.path.expanduser("~/Desktop"), 'New'), exist_ok=True)
    xml_from_xlsx_NBP(os.path.expanduser("~/Desktop/NEW"), "E:/DG-1.xlsx", 'DG-1')
