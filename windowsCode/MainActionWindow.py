from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.GusForms = QtWidgets.QGroupBox(self.centralwidget)
        self.GusForms.setGeometry(QtCore.QRect(0, 0, 500, 330))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.GusForms.setFont(font)
        self.GusForms.setAlignment(QtCore.Qt.AlignCenter)
        self.GusForms.setObjectName("GusForms")
        self.choises = QtWidgets.QWidget(self.GusForms)
        self.choises.setGeometry(QtCore.QRect(0, 10, 330, 150))
        self.choises.setObjectName("choises")
        self.GUS_ChooseFile = QtWidgets.QPushButton(self.choises)
        self.GUS_ChooseFile.setGeometry(QtCore.QRect(180, 90, 120, 30))
        font = QtGui.QFont()
        font.setFamily("qtquickcontrols")
        font.setPointSize(12)
        self.GUS_ChooseFile.setFont(font)
        self.GUS_ChooseFile.setObjectName("GUS_ChooseFile")
        self.chooseGUS_Form = QtWidgets.QComboBox(self.choises)
        self.chooseGUS_Form.setGeometry(QtCore.QRect(180, 30, 120, 30))
        font = QtGui.QFont()
        font.setFamily("qtquickcontrols")
        font.setPointSize(12)
        self.chooseGUS_Form.setFont(font)
        self.chooseGUS_Form.setObjectName("chooseGUS_Form")
        self.chooseGUS_Form.addItem("")
        self.chooseGUS_Form.addItem("")
        self.chooseGUS_Form.addItem("")
        self.chooseGUS_Form.addItem("")
        self.chooseGUS_Form.addItem("")
        self.label_2 = QtWidgets.QLabel(self.choises)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.choises)
        self.label_1.setGeometry(QtCore.QRect(30, 90, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.GUS_SendButton = QtWidgets.QPushButton(self.GusForms)
        self.GUS_SendButton.setGeometry(QtCore.QRect(355, 58, 120, 50))
        font = QtGui.QFont()
        font.setFamily("qtquickcontrols")
        font.setPointSize(12)
        self.GUS_SendButton.setFont(font)
        self.GUS_SendButton.setObjectName("GUS_SendButton")
        self.choises_2 = QtWidgets.QWidget(self.GusForms)
        self.choises_2.setGeometry(QtCore.QRect(0, 160, 500, 170))
        self.choises_2.setObjectName("choises_2")
        self.label = QtWidgets.QLabel(self.choises_2)
        self.label.setGeometry(QtCore.QRect(10, 70, 120, 30))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.choises_2)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 120, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.choises_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 120, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.choises_2)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 120, 30))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.choises_2)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 120, 30))
        self.label_6.setObjectName("label_6")
        self.GUS_Login = QtWidgets.QPlainTextEdit(self.choises_2)
        self.GUS_Login.setGeometry(QtCore.QRect(140, 10, 340, 30))
        self.GUS_Login.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Login.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Login.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.GUS_Login.setReadOnly(False)
        self.GUS_Login.setObjectName("GUS_Login")
        self.GUS_Email = QtWidgets.QPlainTextEdit(self.choises_2)
        self.GUS_Email.setGeometry(QtCore.QRect(140, 70, 340, 30))
        self.GUS_Email.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Email.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Email.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.GUS_Email.setReadOnly(False)
        self.GUS_Email.setObjectName("GUS_Email")
        self.GUS_Password = QtWidgets.QPlainTextEdit(self.choises_2)
        self.GUS_Password.setGeometry(QtCore.QRect(140, 40, 340, 30))
        self.GUS_Password.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Password.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Password.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.GUS_Password.setReadOnly(False)
        self.GUS_Password.setObjectName("GUS_Password")
        self.GUS_Phone = QtWidgets.QPlainTextEdit(self.choises_2)
        self.GUS_Phone.setGeometry(QtCore.QRect(140, 100, 340, 30))
        self.GUS_Phone.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Phone.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Phone.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.GUS_Phone.setReadOnly(False)
        self.GUS_Phone.setObjectName("GUS_Phone")
        self.GUS_Name = QtWidgets.QPlainTextEdit(self.choises_2)
        self.GUS_Name.setGeometry(QtCore.QRect(140, 130, 340, 30))
        self.GUS_Name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.GUS_Name.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.GUS_Name.setReadOnly(False)
        self.GUS_Name.setObjectName("GUS_Name")
        self.GusForms_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.GusForms_2.setGeometry(QtCore.QRect(0, 330, 500, 220))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.GusForms_2.setFont(font)
        self.GusForms_2.setAlignment(QtCore.Qt.AlignCenter)
        self.GusForms_2.setObjectName("GusForms_2")
        self.choises_1 = QtWidgets.QWidget(self.GusForms_2)
        self.choises_1.setGeometry(QtCore.QRect(0, 10, 330, 211))
        self.choises_1.setObjectName("choises_1")
        self.NBP_ChooseFile = QtWidgets.QPushButton(self.choises_1)
        self.NBP_ChooseFile.setGeometry(QtCore.QRect(185, 90, 120, 30))
        font = QtGui.QFont()
        font.setFamily("qtquickcontrols")
        font.setPointSize(12)
        self.NBP_ChooseFile.setFont(font)
        self.NBP_ChooseFile.setObjectName("NBP_ChooseFile")
        self.chooseXML = QtWidgets.QComboBox(self.choises_1)
        self.chooseXML.setGeometry(QtCore.QRect(185, 30, 120, 30))
        font = QtGui.QFont()
        font.setFamily("qtquickcontrols")
        font.setPointSize(12)
        self.chooseXML.setFont(font)
        self.chooseXML.setObjectName("chooseXML")
        self.chooseXML.addItem("")
        self.chooseXML.addItem("")
        self.label_14 = QtWidgets.QLabel(self.choises_1)
        self.label_14.setGeometry(QtCore.QRect(30, 30, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.choises_1)
        self.label_15.setGeometry(QtCore.QRect(30, 90, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.choises_1)
        self.label_16.setGeometry(QtCore.QRect(30, 150, 140, 30))
        self.label_16.setObjectName("label_16")
        self.SheetName = QtWidgets.QPlainTextEdit(self.choises_1)
        self.SheetName.setGeometry(QtCore.QRect(185, 150, 120, 30))
        self.SheetName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SheetName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SheetName.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.SheetName.setReadOnly(False)
        self.SheetName.setObjectName("SheetName")
        self.NBP_CreateButton = QtWidgets.QPushButton(self.GusForms_2)
        self.NBP_CreateButton.setGeometry(QtCore.QRect(360, 90, 120, 50))
        font = QtGui.QFont()
        font.setFamily("qtquickcontrols")
        font.setPointSize(12)
        self.NBP_CreateButton.setFont(font)
        self.NBP_CreateButton.setObjectName("NBP_CreateButton")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuCreate_XML_file_from_xlsx_file = QtWidgets.QAction(self.menuActions)
        self.menuCreate_XML_file_from_xlsx_file.setObjectName("menuCreate_XML_file_from_xlsx_file")
        self.menuCreate_WB_for_specyfic_GUS_forms = QtWidgets.QMenu(self.menuActions)
        self.menuCreate_WB_for_specyfic_GUS_forms.setObjectName("menuCreate_WB_for_specyfic_GUS_forms")
        self.menuSend_values_to_GUS = QtWidgets.QAction(self.menuActions)
        self.menuSend_values_to_GUS.setObjectName("menuSend_values_to_GUS")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionAdd_file = QtWidgets.QAction(self)
        self.actionAdd_file.setText("Add File")
        self.actionAdd_file.setStatusTip("")
        self.actionAdd_file.setAutoRepeat(True)
        self.actionAdd_file.setObjectName("actionAdd_file")
        self.actionGet_File = QtWidgets.QAction(self)
        self.actionGet_File.setObjectName("actionGet_File")
        self.actionSort_Values = QtWidgets.QAction(self)
        self.actionSort_Values.setObjectName("actionSort_Values")
        self.action_Keep_alive_mode = QtWidgets.QAction(self)
        self.action_Keep_alive_mode.setObjectName("action_Keep_alive_mode")
        self.actionMPZ_KRH = QtWidgets.QAction(self)
        self.actionMPZ_KRH.setObjectName("actionMPZ_KRH")
        self.actionMAZ_KRH = QtWidgets.QAction(self)
        self.actionMAZ_KRH.setObjectName("actionMAZ_KRH")
        self.actionSP_ = QtWidgets.QAction(self)
        self.actionSP_.setObjectName("actionSP_")
        self.actionF_01 = QtWidgets.QAction(self)
        self.actionF_01.setObjectName("actionF_01")
        self.actionRF_01 = QtWidgets.QAction(self)
        self.actionRF_01.setObjectName("actionRF_01")
        self.actionC_01 = QtWidgets.QAction(self)
        self.actionC_01.setObjectName("actionC_01")
        self.actionDG_1 = QtWidgets.QAction(self)
        self.actionDG_1.setObjectName("actionDG_1")
        self.actionEmail = QtWidgets.QAction(self)
        self.actionEmail.setObjectName("actionEmail")
        self.actionContact = QtWidgets.QAction(self)
        self.actionContact.setObjectName("actionContact")
        self.menuFiles.addAction(self.actionAdd_file)
        self.menuFiles.addAction(self.actionGet_File)
        self.menuCreate_WB_for_specyfic_GUS_forms.addAction(self.actionSP_)
        self.menuCreate_WB_for_specyfic_GUS_forms.addAction(self.actionC_01)
        self.menuCreate_WB_for_specyfic_GUS_forms.addAction(self.actionF_01)
        self.menuCreate_WB_for_specyfic_GUS_forms.addAction(self.actionDG_1)
        self.menuCreate_WB_for_specyfic_GUS_forms.addAction(self.actionRF_01)
        self.menuActions.addAction(self.actionSort_Values)
        self.menuActions.addAction(self.menuCreate_XML_file_from_xlsx_file)
        self.menuActions.addAction(self.menuCreate_WB_for_specyfic_GUS_forms.menuAction())
        self.menuActions.addAction(self.menuSend_values_to_GUS)
        self.menuActions.addAction(self.action_Keep_alive_mode)
        self.menuHome.addAction(self.actionContact)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GusForms.setTitle(_translate("MainWindow", "Gus Forms"))
        self.GUS_ChooseFile.setText(_translate("MainWindow", "Choose File"))
        self.chooseGUS_Form.setItemText(0, _translate("MainWindow", "C-01"))
        self.chooseGUS_Form.setItemText(1, _translate("MainWindow", "F-01"))
        self.chooseGUS_Form.setItemText(2, _translate("MainWindow", "DG-1"))
        self.chooseGUS_Form.setItemText(3, _translate("MainWindow", "RF-01"))
        self.chooseGUS_Form.setItemText(4, _translate("MainWindow", "SP"))
        self.label_2.setText(_translate("MainWindow", "Choose Form"))
        self.label_1.setText(_translate("MainWindow", "Choose File"))
        self.GUS_SendButton.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Phone"))
        self.label_4.setText(_translate("MainWindow", "Login"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "Name"))
        self.GusForms_2.setTitle(_translate("MainWindow", "NBP XMLs"))
        self.NBP_ChooseFile.setText(_translate("MainWindow", "Choose File"))
        self.chooseXML.setItemText(0, _translate("MainWindow", "MAZ_KRH"))
        self.chooseXML.setItemText(1, _translate("MainWindow", "MPZ_KRH"))
        self.label_14.setText(_translate("MainWindow", "Choose XML"))
        self.label_15.setText(_translate("MainWindow", "Choose File"))
        self.label_16.setText(_translate("MainWindow", "Set sheet name"))
        self.SheetName.setPlainText(_translate("MainWindow", "Arkusz1"))
        self.NBP_CreateButton.setText(_translate("MainWindow", "Create"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.menuCreate_XML_file_from_xlsx_file.setText(_translate("MainWindow", "Create XML file from .xlsx file"))
        self.menuCreate_WB_for_specyfic_GUS_forms.setTitle(_translate("MainWindow", "Create WB  for specyfic GUS forms"))
        self.menuSend_values_to_GUS.setText(_translate("MainWindow", "Send values to GUS"))
        self.menuHome.setTitle(_translate("MainWindow", "Help"))
        self.actionAdd_file.setIconText(_translate("MainWindow", "Add File"))
        self.actionAdd_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionGet_File.setText(_translate("MainWindow", "Move File"))
        self.actionGet_File.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSort_Values.setText(_translate("MainWindow", "Sort Values in WB"))
        self.action_Keep_alive_mode.setText(_translate("MainWindow", "Enter *Keep alive mode*"))
        self.actionMPZ_KRH.setText(_translate("MainWindow", "MPZ_KRH"))
        self.actionMAZ_KRH.setText(_translate("MainWindow", "MAZ_KRH"))
        self.actionSP_.setText(_translate("MainWindow", "SP"))
        self.actionF_01.setText(_translate("MainWindow", "F-01"))
        self.actionRF_01.setText(_translate("MainWindow", "RF-01"))
        self.actionC_01.setText(_translate("MainWindow", "C-01"))
        self.actionDG_1.setText(_translate("MainWindow", "DG-1"))
        self.actionEmail.setText(_translate("MainWindow", "Email"))
        self.actionContact.setText(_translate("MainWindow", "Contact Me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
