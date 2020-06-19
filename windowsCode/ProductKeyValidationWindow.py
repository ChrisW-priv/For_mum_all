from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('KeyValidationWindow')
        self.setupUi()

    def setupUi(self):
        mainWidth =720
        mainHeight=480
        self.setObjectName("MainWindow")
        self.resize(mainWidth, mainHeight)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        boxWidth=500
        boxHeight=250
        self.KeyValidationBox = QtWidgets.QGroupBox(self.centralwidget)
        self.KeyValidationBox.setEnabled(True)
        self.KeyValidationBox.setGeometry(QtCore.QRect( int((mainWidth-boxWidth)/2), int((mainHeight-boxHeight)/2), boxWidth, boxHeight))
        self.KeyValidationBox.setObjectName("KeyValidationBox")
        
        self.Message = QtWidgets.QLabel(self.KeyValidationBox)
        self.Message.setEnabled(True)
        self.Message.setGeometry(QtCore.QRect( int((boxWidth-400)/2), 30, 400, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Message.setFont(font)
        self.Message.setTextFormat(QtCore.Qt.AutoText)
        self.Message.setAlignment(QtCore.Qt.AlignCenter)
        self.Message.setObjectName("Message")
        
        self.ProdKeyInput = QtWidgets.QLineEdit(self.KeyValidationBox)
        self.ProdKeyInput.setGeometry(QtCore.QRect( int((boxWidth-400)/2), 100, 350, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ProdKeyInput.setFont(font)
        self.ProdKeyInput.setAlignment(QtCore.Qt.AlignHCenter)
        self.ProdKeyInput.setObjectName("ProdKeyInput")
        
        self.Submit = QtWidgets.QPushButton(self.KeyValidationBox)
        self.Submit.setGeometry(QtCore.QRect( int((boxWidth-400)/2)+350+10, 107, 80, 34))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75) 
        self.Submit.setFont(font)
        self.Submit.setObjectName("Submit")

        self.GenerateNewKey = QtWidgets.QPushButton(self.KeyValidationBox)
        self.GenerateNewKey.setGeometry(QtCore.QRect( int((boxWidth-200)/2), 170, 200, 45))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.GenerateNewKey.setFont(font)
        self.GenerateNewKey.setObjectName("GenerateNewKey")
        
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 18))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Message.setText(_translate("MainWindow", "Enter your produkt key:"))
        self.Submit.setText(_translate("MainWindow", "Submit"))
        self.GenerateNewKey.setText(_translate("MainWindow", "Generate New Key"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
