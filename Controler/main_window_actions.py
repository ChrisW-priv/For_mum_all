from Logic import wb_form_f01, wb_form_c01, wb_form_gd1, wb_form_sp, wb_form_rf01
from windowsCode.MainWindow import MainWindow as Main

def main_window_actions(self):
	self.main = Main()
	self.main.show()
	
	# actions	
	self.main.WybierzPlik_GUS.connect(choose_GUS_file_to_be_converted)
	self.main.CreateXML_GUS.connect(self.create_XML_GUS)
	self.main.SendToGus.connect(self.send_values_to_GUS)
	self.main.WybierzPlik_GUS_2.connect(choose_GUS_file_to_be_send)
	self.main.WybierzPlik_NBP.connect(choose_NBP_file_to_be_converted)
	self.main.CreateXML_NBP.connect(self.create_XML_NBP)

	def choose_GUS_file_to_be_converted():
		self.GUS_file_to_be_converted = QFileDialog.getOpenFileName(caption='choose_file')
	def choose_GUS_file_to_be_send():
		self.GUS_file_to_be_send = QFileDialog.getOpenFileName(caption='choose_file')
	def choose_NBP_file_to_be_converted():
		self.NBP_file_to_be_converted = QFileDialog.getOpenFileName(caption='choose_file')
