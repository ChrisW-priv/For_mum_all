from PyQt5 import QtWidgets
from Controler import Controler

def main():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	controller = Controler()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
