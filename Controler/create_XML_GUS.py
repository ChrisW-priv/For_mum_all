from Logic import xml_from_xlsx_GUS

def create_XML_GUS(self):
	form = str(self.main.GUS_Form_to_XML.currentText())
	sheet_name = str(self.main.GUS_sheetname.text())
	
	try:
		assert file != ''
		assert sheet_name != ''
		file = self.GUS_file_to_be_converted[0]
		xml_from_xlsx_GUS(self.path_to_desktop, file, form, sheet_name)
		self.show_info_popup('FileCreated!', 'Your file has been created!')
	except AssertionError:
		if file == '':
			self.show_info_popup('FileNotSetError!', 'You have not chosen any file!')
		if sheet_name == '':
			self.show_info_popup('SheetNameNotSetError!', 'You have not set sheet name!')
	except Exception:
		self.show_info_popup('UnkownError!', 'There has been some error in the code,'\
			'\nin this case most probably wrong type of file or sheetname was chosen')
