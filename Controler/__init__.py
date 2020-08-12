class Controler:
	def __init__(self):
		self.main_window_actions()
		self.set_begin()
	
	from .main_window_actions import main_window_actions
	from .setup_files import gus_file, nbp_file, set_file, set_begin
	from .sort_file import sort_file
	from .send_values_to_GUS import send_values_to_GUS
	from .create_XML_NBP import create_XML_NBP
	from .show_popup import show_popup
