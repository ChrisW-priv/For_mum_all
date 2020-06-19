def make_xml_from_xlsx(original_file='Form_name (date-format).xlsx', sheet_name='Arkusz1'):
    import xml.etree.ElementTree as ET
    import pandas as pd
    import datetime

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
    content_setup = {'dataWypelnienia': f"{str(df.at[0, 'dataWypelnienia']).split(' ')[0]}",
                     'xsi:type': f"ts:Spr{original_file.split('/')[-1].split(' ')[0]}Type"}
    header_setup = {'td:regon': '63027533800000',
                    'ts:nazwa': 'Tarkett Polska Sp. z o.o.'}

    package = ET.Element('prz:przesylka')
    content = ET.SubElement(package, 'prz:sprawozdanie')
    header = ET.SubElement(content, 'ts:naglowek')
    data = ET.SubElement(content, 'ts:dane')
    rows = ET.SubElement(data, 'ts:wiersze')

    for key, value in package_setup.items():
        package.set(key, value)

    for key, value in content_setup.items():
        content.set(key, value)

    for key, value in header_setup.items():
        header_element = ET.SubElement(header, key)
        header_element.text = value

    for line in range(df.shape[0]):
        try:
            # sometimes it will be 'NoneType' which breaks everything
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

    now = datetime.datetime.now()
    new_file = f"{original_file.split('/')[-1].split(' ')[0]}_{now.strftime('%m_%Y')}_dane.xml"
    mydata = ET.tostring(package)
    myfile = open(new_file, "wb")
    myfile.write(mydata)
