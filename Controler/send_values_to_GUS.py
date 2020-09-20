from Logic.GUS.send_XML_to_GUS import send_XML_to_GUS
from Logic.GUS.GUS_Sender import GUSAutomated


def send_values_to_GUS(self):
	id_ = str(self.main.GUS_LOGIN.toPlainText())
	pwd = str(self.main.GUS_PWD.toPlainText())
	form = str(self.main.GUS_Form_Send.currentText())
	try:
		file = str((self.GUS_file_to_be_send)[0])
	except Exception:
		file = ''

	try: 
		assert id_ != '' and pwd != ''
		assert file != ''

		try:
			b = GUSAutomated(id_, pwd)
			b.choose_form(form)

			if form == 'C-01':
				b.c01(file)
			elif form == 'RF-01':
				b.rf01(file)
			elif form == 'F-01':
				b.f01(file)
			elif form == 'DG-1':
				b.dg1(file)
			elif form == 'SP':
				b.sp(file)
			else:
				self.show_info_popup('InvalidFormError!', 'Current Logic does not support form you have chosen')
		except Exception as e:
			self.show_info_popup('UnknownError', e)
	except Exception as e:
		if file == '':
			self.show_info_popup('FileNotSetError!', 'You have not chosen any file!')
		if id_ == '' or pwd == '':
			self.show_info_popup('IdOrPasswordNotSet!', 'You have not set your Id or Password!')		
		if file != '' and id_ != '' and pwd != '':
			self.show_info_popup('UnknownError!', f'Sth unexpected happened!\nError: "{e}"')
