def generate_new_key(self):
	from windowsCode.GenerateKeyWindow import MainWindow as Window
	import secrets, json 

	win = Window()
	self.validationPage.close()
	win.show()

	with open(self.setup_file_name) as f:
		data = json.load(f)

	pwd = data['email_pwd']
	user_name = data['user_name']
	user_email = str(win.EmailInput.toPlainText())
	new_key = secrets.token_hex(16)
	
	def c():
		send_email(pwd, user_name, user_email, new_key)
		
		data['key'] = new_key
		with open(self.setup_file_name, 'w') as f:
			json.dump(data, f)
		
		win.close()
		self.validationPage.show()

		self.show_popup('KeyHasBeenGenerated','Your Key has been generated - wait for our team to validate it and send it to your email')

	win.GenerateKey.clicked.connect(c) 


def send_email(pwd, user_name, user_email, new_key):
	import smtplib
	from email.message import EmailMessage

	email = 'kw.python.testing@gmail.com'

	msg = EmailMessage()
	msg['From'] = email
	msg['To'] = email
	msg['Subject'] = f'New key for {user_name}'
	msg.set_content(f'New key has been created for user with email: {user_email}\nNew key is: {new_key}')
	try:
		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			smtp.login(email, pwd)
			smtp.send_message(msg)
	except Exception:
		from PyQt5.QtWidgets import QMessageBox
		msg = QMessageBox()
		msg.setWindowTitle('EmailPwdNotSet!')
		msg.setText('Contact our team cuz they f@#$ up and forgot to add special key to whole setup :-(')
		msg.setIcon(QMessageBox.Information)		
		x = msg.exec_()
