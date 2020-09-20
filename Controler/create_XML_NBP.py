from Logic import xml_from_xlsx_NBP

def create_XML_NBP(self):
	form = str(self.main.chooseXML.currentText())
	sheet_name = str(self.main.SheetName.toPlainText())

	try:
		assert file != ''
		assert sheet_name != ''
		file = self.NBP_file_to_be_converted[0]
		xml_from_xlsx_NBP(self.path_to_desktop, file, form, sheet_name)
		self.show_info_popup('FileCreated!', 'Your file has been created!')
	except AssertionError:
		if file == '':
			self.show_info_popup('FileNotSetError!', 'You have not chosen any file!')
		if sheet_name == '':
			self.show_info_popup('SheetNameNotSetError!', 'You have not set sheet name!')
	except Exception:
		self.show_info_popup('UnkownError!', 'There has been some error in the code,'\
			'\nin this case most probably wrong type of file or sheetname was chosen')
