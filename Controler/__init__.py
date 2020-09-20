import os

class Controler:
    def __init__(self):
        self.main_window_actions()
        # setup
        self.path_to_desktop = os.path.join(os.path.expanduser("~/Desktop"), 'New')
        os.makedirs(self.path_to_desktop, exist_ok=True)

        self.GUS_file_to_be_converted = ''
        self.GUS_file_to_be_send = ''
        self.NBP_file_to_be_converted = ''
    
    from .show_popup import show_info_popup
    from .main_window_actions import main_window_actions
    from .create_XML_NBP import create_XML_NBP
    from .create_XML_GUS import create_XML_GUS
    from .send_values_to_GUS import send_values_to_GUS
