from windowsCode.MainActionWindow import MainWindow as Main
from windowsCode.ProductKeyValidationWindow import MainWindow as Validation
from Logic import sort, keep_alive, GUSAutomated, make_xml_from_xlsx, wb_form_f01, wb_form_c01, wb_form_gd1, wb_form_sp, wb_form_rf01
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

	def show_main(self):
		self.main = Main()
		self.validationPage.close()
		self.main.show()
		self.main_actions()

	def main_actions(self):
		self.main.actionSort_Values.triggered.connect(lambda: sort(self.current_file, list_=['ns3:rodzPowKap', 'ns3:kraj', 'ns3:waluta']))
		self.main.action_Keep_alive_mode.triggered.connect(keep_alive)
		self.main.actionContact.triggered.connect(self.contact_info)

		self.main.GUS_ChooseFile.clicked.connect(self.choose_file)
		self.main.GUS_SendButton.clicked.connect(self.send_values_to_GUS)
		self.main.menuSend_values_to_GUS.triggered.connect(self.send_values_to_GUS)

		self.main.NBP_ChooseFile.clicked.connect(self.choose_file)
		self.main.NBP_CreateButton.clicked.connect(self.create_XML_NBP)
		self.main.menuCreate_XML_file_from_xlsx_file.triggered.connect(self.create_XML_NBP)

		self.main.actionAdd_file.triggered.connect(self.choose_file)
		self.main.actionSP_.triggered.connect(wb_form_sp)
		self.main.actionF_01.triggered.connect(wb_form_f01)
		self.main.actionRF_01.triggered.connect(wb_form_rf01)
		self.main.actionC_01.triggered.connect(wb_form_c01)
		self.main.actionDG_1.triggered.connect(wb_form_gd1)

	def contact_info(self):
		print('Contact info will be aded!')
	
	def send_values_to_GUS(self):
		id_ = str(self.main.GUS_Login.toPlainText())
		pwd = str(self.main.GUS_Password.toPlainText())
		email = str(self.main.GUS_Email.toPlainText())
		phone = str(self.main.GUS_Phone.toPlainText())
		name = str(self.main.GUS_Name.toPlainText())
		form = str(self.main.chooseGUS_Form.currentText())
		file = str(self.current_file)
		
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

	def create_XML_NBP(self):
		file = self.current_file
		form = str(self.main.chooseXML.currentText())
		sheet_name = str(self.main.SheetName.toPlainText())

		make_xml_from_xlsx(file, form, sheet_name)

	def choose_file(self):
		self.current_file = QtWidgets.QFileDialog.getOpenFileName(caption='choose_file')


def main():
	app = QtWidgets.QApplication(sys.argv)
	controller = Controller()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
