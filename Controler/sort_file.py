def sort_file(self):
	try:
		assert self.current_file != ''
		sort(self.current_file, list_=['ns3:rodzPowKap', 'ns3:kraj', 'ns3:waluta'])
	except Exception:
		from PyQt5.QtWidgets import QMessageBox

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
