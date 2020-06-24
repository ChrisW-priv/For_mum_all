def sort_file(self):
	from PyQt5.QtWidgets import QMessageBox

	try:
		assert self.current_file != ''
		sort(self.current_file[0], list_=['ns3:rodzPowKap', 'ns3:kraj', 'ns3:waluta'])

		msg = QMessageBox()
		msg.setWindowTitle('FileSorted!')
		msg.setText('File sorted in palce!')
		msg.setIcon(QMessageBox.Information)		
		x = msg.exec_()
	except Exception:
		if self.current_file == '':
			msg = QMessageBox()
			msg.setWindowTitle('FileNotSetError!')
			msg.setText('You have not chosen any file!')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()
		else:
			msg = QMessageBox()
			msg.setWindowTitle('UnkownError!')
			msg.setText('There has been some error in the code,\nin this case most probably wrong type of file was chosen')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()
