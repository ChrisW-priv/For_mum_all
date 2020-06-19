from windowsCode.MainActionWindow import MainWindow as Main
from windowsCode.ProductKeyValidationWindow import MainWindow as Validation
from Logic import GUSAutomated
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json


class Controller:
	def __init__(self):
		with open('setup.json') as f:
			self.jsonf = json.load(f)
		self.current_file = ''
		self.validation_page()
		
	def validation_page(self):
		self.validationPage = Validation()
		self.validationPage.Submit.clicked.connect(self.submit_key)
		self.validationPage.ProdKeyInput.returnPressed.connect(self.submit_key)
		self.validationPage.GenerateNewKey.clicked.connect(self.generate_new_key)
		self.validationPage.show()

	def show_main(self):
		self.main = Main()
		self.validationPage.close()
		self.main.show()
		self.main_actions()

	def main_actions(self):
		self.main.GUS_ChooseFile.clicked.connect(self.choose_file)
		self.main.GUS_SendButton.clicked.connect(self.run_send_values_to_GUS)

	def send_values_to_GUS(self, id_, pwd, email, phone, name, form, file):
		b = GUSAutomated(id_, pwd, email, phone, name)
		
		if form == 'C-01':
			b.choose_form(form)
			b.c01(file)
		elif form == 'RF-01':
			b.choose_form(form)
			b.rf01(file)
		elif form == 'F-01':
			b.choose_form(form)
			b.f01(file)
		elif form == 'DG-1':
			b.choose_form(form)
			b.dg1(file)
		elif form == 'SP':
			b.choose_form(form)
			b.sp(file)
		else:
			msg = QMessageBox()
			msg.setWindowTitle('InvalidFormError!')
			msg.setText('Current Logic does not support form u have chosen')
			msg.setIcon(QMessageBox.Information)		
			x = msg.exec_()

	def run_send_values_to_GUS(self):
		id_ = str(self.main.GUS_Login.toPlainText())
		pwd = str(self.main.GUS_Password.toPlainText())
		email = str(self.main.GUS_Email.toPlainText())
		phone = str(self.main.GUS_Phone.toPlainText())
		name = str(self.main.GUS_Name.toPlainText())
		form = str(self.main.chooseGUS_Form.currentText())
		file = str(self.current_file)
		self.send_values_to_GUS(id_, pwd, email, phone, name, form, file)

	def choose_file(self):
		self.current_file = QtWidgets.QFileDialog.getOpenFileName(caption='choose_file')

	def submit_key(self):        
		key_input = self.validationPage.ProdKeyInput.text()
		
		if key_input == self.jsonf['key']:
			self.show_main()
		else:	
			msg = QMessageBox()
			msg.setWindowTitle('KeyValidationError!')
			msg.setText('Key input does not match the Produkt Key')
			msg.setIcon(QMessageBox.Information)
			
			x = msg.exec_()

	def generate_new_key(self):
		print('Will be generated!!!')


def main():
	app = QtWidgets.QApplication(sys.argv)
	controller = Controller()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
