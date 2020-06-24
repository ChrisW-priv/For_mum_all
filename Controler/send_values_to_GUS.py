from Logic import GUSAutomated

def send_values_to_GUS(self):
	id_ = str(self.main.GUS_Login.toPlainText())
	pwd = str(self.main.GUS_Password.toPlainText())
	email = str(self.main.GUS_Email.toPlainText())
	phone = str(self.main.GUS_Phone.toPlainText())
	name = str(self.main.GUS_Name.toPlainText())
	form = str(self.main.chooseGUS_Form.currentText())
	file = self.GUS_File				
	
	try: 
		assert id_ != '' and pwd != ''
		assert file != ''

		try:
			b = GUSAutomated(id_, pwd, email, phone, name)
			
			if form == 'C-01':
				b.choose_form(form)
				b.c01(file[0])
			elif form == 'RF-01':
				b.choose_form(form)
				b.rf01(file[0])
			elif form == 'F-01':
				b.choose_form(form)
				b.f01(file[0])
			elif form == 'DG-1':
				b.choose_form(form)
				b.dg1(file[0])
			elif form == 'SP':
				b.choose_form(form)
				b.sp(file[0])
			else:
				from PyQt5.QtWidgets import QMessageBox
				msg = QMessageBox()
				msg.setWindowTitle('InvalidFormError!')
				msg.setText('Current Logic does not support form you have chosen')
				msg.setIcon(QMessageBox.Information)		
				x = msg.exec_()
		except Exception:
			from PyQt5.QtWidgets import QMessageBox

			msg = QMessageBox()
			msg.setWindowTitle('UnknownError')
			msg.setText('This was unexpected\nMost likely you have set invalid password or id')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()
	except Exception:
		from PyQt5.QtWidgets import QMessageBox

		if id_ == '' or pwd == '':
			msg = QMessageBox()
			msg.setWindowTitle('IdOrPasswordNotSet!')
			msg.setText('You have not set your Id or Password!')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()
		if file == '':
			msg = QMessageBox()
			msg.setWindowTitle('FileNotSetError!')
			msg.setText('You have not chosen any file!')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()
		else:
			msg = QMessageBox()
			msg.setWindowTitle('UnknownError!')
			msg.setText('Sth unexpected happened!')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()
