from PyQt5.QtWidgets import QFileDialog

def gus_file(self):
	self.GUS_File = QFileDialog.getOpenFileName(caption='choose_file')
def nbp_file(self):
	self.NBP_File = QFileDialog.getOpenFileName(caption='choose_file')
def set_file(self):
	self.current_file = QFileDialog.getOpenFileName(caption='choose_file')
	self.GUS_File = self.current_file
	self.NBP_File = self.current_file