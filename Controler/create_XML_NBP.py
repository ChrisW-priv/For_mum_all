from Logic import xml_from_xlsx_NBP

def create_XML_NBP(self):
	form = str(self.main.NBPForm.currentText())
	sheet_name = str(self.main.NBP_sheetname.text())

	try:
		assert self.NBP_file_to_be_converted != ''
		assert sheet_name != ''
		file = self.NBP_file_to_be_converted[0]
		xml_from_xlsx_NBP(self.path_to_desktop, file, form, sheet_name)
		self.show_info_popup('FileCreated!', 'Your file has been created!')
	except AssertionError:
		if self.NBP_file_to_be_converted == '':
			self.show_info_popup('FileNotSetError!', 'You have not chosen any file!')
		if sheet_name == '':
			self.show_info_popup('SheetNameNotSetError!', 'You have not set sheet name!')
	except Exception as e:
		self.show_info_popup('UnkownError!', str(e))
