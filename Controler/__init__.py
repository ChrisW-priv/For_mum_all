class Controler:
	def __init__(self):
		import json

		with open('setup.json') as f:
			self.jsonf = json.load(f)
		
		# file setup
		self.current_file = ''
		self.GUS_File = ''
		self.NBP_File = ''
		
		# all good now show firt window
		self.validation_page()
	
	from .validation_page import validation_page
	from .submit_key import submit_key
	from .generate_new_key import generate_new_key
	from .main_window_actions import main_window_actions
	from .setup_files import gus_file, nbp_file, set_file
	from .sort_file import sort_file
	from .send_values_to_GUS import send_values_to_GUS
	from .create_XML_NBP import create_XML_NBP
	from .contact_info import contact_info
