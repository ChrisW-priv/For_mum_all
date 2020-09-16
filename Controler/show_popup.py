def show_info_popup(self, title, msg):
	from PyQt5.QtWidgets import QMessageBox

	popup = QMessageBox()
	popup.setWindowTitle(title)
	popup.setText(msg)
	popup.setIcon(QMessageBox.Information)		
	x = popup.exec_()