from Logic import make_xml_from_xlsx

def create_XML_NBP(self):
	file = self.NBP_File
	form = str(self.main.chooseXML.currentText())
	sheet_name = str(self.main.SheetName.toPlainText())

	try:
		assert file != ''
		assert sheet_name != ''
		
		make_xml_from_xlsx(file, form, sheet_name)
	except Exception:
		from PyQt5.QtWidgets import QMessageBox

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