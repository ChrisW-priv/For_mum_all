from Logic.GUS.GUS_Sender import GUSAutomated

def send_XML_to_GUS(file, form, login, pwd):
	try:
		b = GUSAutomated(login, pwd)
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
