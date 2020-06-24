def submit_key(self):
	import json
	
	key_input = self.validationPage.ProdKeyInput.text()
	
	with open(self.setup_file_name) as f:
		data = json.load(f)

	if key_input == data['key']:
		self.validationPage.close()
		self.main_window_actions()
	else:	
		self.show_popup('KeyValidationError!', 'Key input does not match the Produkt Key')