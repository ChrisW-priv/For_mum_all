from Logic import xml_from_xlsx_GUS

def create_XML_GUS(self):
	form = str(self.main.chooseXML.currentText())
	sheet_name = str(self.main.SheetName.toPlainText())
	try:
		file = self.NBP_File[0]
	except Exception:
		file = ''

	try:
		assert file != ''
		assert sheet_name != ''
		
		xml_from_xlsx_GUS(file, form, sheet_name)

		self.show_info_popup('FileCreated!', 'Your file has been created!')
	except Exception:
		if file == '':
			self.show_info_popup('FileNotSetError!', 'You have not chosen any file!')
		if sheet_name == '':
			self.show_info_popup('SheetNameNotSetError!', 'You have not chosen sheet name!')
		else:
			self.show_info_popup('UnkownError!', 'There has been some error in the code,'\
				'\nin this case most probably wrong type of file or sheetname was chosen')
