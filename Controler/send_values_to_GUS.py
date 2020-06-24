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
				self.show_popup('InvalidFormError!', 'Current Logic does not support form you have chosen')
		except Exception:
			self.show_popup('UnknownError', 'This was unexpected\nMost likely you have set invalid password or id\n'\
				'or your file was not set correctly, try using one created with this app')
	except Exception as e:
		if file == '':
			self.show_popup('FileNotSetError!', 'You have not chosen any file!')
		if id_ == '' or pwd == '':
			self.show_popup('IdOrPasswordNotSet!', 'You have not set your Id or Password!')		
		if file != '' and id_ != '' and pwd != '':
			self.show_popup('UnknownError!', f'Sth unexpected happened!\nError: "{e}"')
