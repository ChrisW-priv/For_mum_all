from Logic import make_xml_from_xlsx

def create_XML_NBP(self):
	from PyQt5.QtWidgets import QMessageBox
	
	form = str(self.main.chooseXML.currentText())
	sheet_name = str(self.main.SheetName.toPlainText())
	try:
		file = self.NBP_File[0]
	except Exception:
		file = ''

	try:
		assert file != ''
		assert sheet_name != ''
		
		make_xml_from_xlsx(file, form, sheet_name)

		msg = QMessageBox()
		msg.setWindowTitle('FileCreated!')
		msg.setText('Your file has been created!')
		msg.setIcon(QMessageBox.Information)		
		x = msg.exec_()
	except Exception:
		if file == '':
			msg = QMessageBox()
			msg.setWindowTitle('FileNotSetError!')
			msg.setText('You have not chosen any file!')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()
		if sheet_name == '':
			msg = QMessageBox()
			msg.setWindowTitle('SheetNameNotSetError!')
			msg.setText('You have not chosen sheet name!')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()
		else:
			msg = QMessageBox()
			msg.setWindowTitle('UnkownError!')
			msg.setText('There has been some error in the code,\nin this case most probably wrong type of file or sheetname was chosen')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()

