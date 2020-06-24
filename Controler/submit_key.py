def submit_key(self):
	key_input = self.validationPage.ProdKeyInput.text()
	
	if key_input == self.jsonf['key']:
		self.main_window_actions()
	else:	
		from PyQt5.QtWidgets import QMessageBox

		msg = QMessageBox()
		msg.setWindowTitle('KeyValidationError!')
		msg.setText('Key input does not match the Produkt Key')
		msg.setIcon(QMessageBox.Information)
		
		x = msg.exec_()