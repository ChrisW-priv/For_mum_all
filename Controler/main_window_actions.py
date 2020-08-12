from Logic import wb_form_f01, wb_form_c01, wb_form_gd1, wb_form_sp, wb_form_rf01
from windowsCode.MainActionWindow import MainWindow as Main

def main_window_actions(self):
	self.main = Main()
	self.main.show()
	
	# actions
	self.main.actionAdd_file.triggered.connect(self.set_file)
	
	self.main.actionSort_Values.triggered.connect(self.sort_file)
	self.main.actionSP_.triggered.connect(wb_form_sp)
	self.main.actionF_01.triggered.connect(wb_form_f01)
	self.main.actionRF_01.triggered.connect(wb_form_rf01)
	self.main.actionC_01.triggered.connect(wb_form_c01)
	self.main.actionDG_1.triggered.connect(wb_form_gd1)

	self.main.GUS_ChooseFile.clicked.connect(self.gus_file)
	self.main.GUS_SendButton.clicked.connect(self.send_values_to_GUS)
	self.main.menuSend_values_to_GUS.triggered.connect(self.send_values_to_GUS)

	self.main.NBP_ChooseFile.clicked.connect(self.nbp_file)
	self.main.NBP_CreateButton.clicked.connect(self.create_XML_NBP)
	self.main.menuCreate_XML_file_from_xlsx_file.triggered.connect(self.create_XML_NBP)
