if __name__ == '__main__':
	from PyQt5.QtWidgets import QApplication
	from Controler import Controler
	import sys

	app = QApplication(sys.argv)
	controller = Controler()
	sys.exit(app.exec_())
