from Logic.GUS.send_XML_to_GUS import send_XML_to_GUS

def send_file_to_GUS(self):
	login = str(self.main.GUS_LOGIN.text())
	pwd = str(self.main.GUS_PWD.text())
	form = str(self.main.GUS_Form_Send.currentText())

	try: 
		assert self.GUS_file_to_be_send != ''
		assert login != '' and pwd != ''
		file = (self.GUS_file_to_be_send)[0]
		send_XML_to_GUS(file, form, login, pwd)
	except AssertionError:
		if self.GUS_file_to_be_send == '':
			self.show_info_popup('FileNotSetError!', 'You have not chosen any file!')
		if login == '' or pwd == '':
			self.show_info_popup('IdOrPasswordNotSet!', 'You have not set your Id or Password!')		
	except Exception as e:
		self.show_info_popup('UnknownError!', f'Sth unexpected happened!\nError: "{e}"')
