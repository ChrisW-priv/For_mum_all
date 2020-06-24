class Controler:
	def __init__(self):
		self.setup_file_name = 'setup.json'
		
		self.overwrite_current_key()
		self.set_begin()		
		# Normally we use line below to validate customer for now we will use the one below that
		# self.validation_page()
		self.main_window_actions()
	
	from .validation_page import validation_page
	from .submit_key import submit_key
	from .generate_new_key import generate_new_key
	from .main_window_actions import main_window_actions
	from .setup_files import gus_file, nbp_file, set_file, set_begin
	from .sort_file import sort_file
	from .send_values_to_GUS import send_values_to_GUS
	from .create_XML_NBP import create_XML_NBP
	from .contact_info import contact_info
	from .show_popup import show_popup
	from .overwrite_current_key import overwrite_current_key
