from Controler.create_XML_GUS import create_XML_GUS
from Controler.create_XML_NBP import create_XML_NBP
from Controler.send_values_to_GUS import send_XML_to_GUS

def main_window_actions(self):
	from PyQt5.QtWidgets import QFileDialog

	def choose_GUS_file_to_be_converted():
		self.GUS_file_to_be_converted = QFileDialog.getOpenFileName(caption='choose_file')
	def choose_GUS_file_to_be_send():
		self.GUS_file_to_be_send = QFileDialog.getOpenFileName(caption='choose_file')
	def choose_NBP_file_to_be_converted():
		self.NBP_file_to_be_converted = QFileDialog.getOpenFileName(caption='choose_file')
	
	# actions	
	self.main.WybierzPlikGUS_ToXML.clicked.connect(choose_GUS_file_to_be_converted)
	self.main.CreateXML_GUS.clicked.connect(self.create_XML_GUS)
	self.main.SendToGus.clicked.connect(self.send_XML_to_GUS)
	self.main.WybierzPlik_GUS_ToSend.clicked.connect(choose_GUS_file_to_be_send)
	self.main.WybierzPlik_NBP.clicked.connect(choose_NBP_file_to_be_converted)
	self.main.CreateXML_NBP.clicked.connect(self.create_XML_NBP)
