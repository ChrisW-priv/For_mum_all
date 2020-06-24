from windowsCode.ProductKeyValidationWindow import MainWindow as Validation

def validation_page(self):
	self.validationPage = Validation()
	
	self.validationPage.Submit.clicked.connect(self.submit_key)
	self.validationPage.ProdKeyInput.returnPressed.connect(self.submit_key)
	
	self.validationPage.GenerateNewKey.clicked.connect(self.generate_new_key)
	
	self.validationPage.show()
