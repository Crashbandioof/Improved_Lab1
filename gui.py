# Form implementation generated from reading ui file 'vote_menu.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_vote_menu = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_vote_menu.setGeometry(QtCore.QRect(240, 10, 61, 16))
        self.label_vote_menu.setObjectName("label_vote_menu")
        self.pushButton_vote = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_vote.setGeometry(QtCore.QRect(150, 40, 56, 17))
        self.pushButton_vote.setObjectName("pushButton_vote")
        self.pushButton_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(300, 40, 56, 17))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.radioButton_John = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_John.setGeometry(QtCore.QRect(150, 80, 62, 14))
        self.radioButton_John.setObjectName("radioButton_John")
        self.radioButton_Jane = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_Jane.setGeometry(QtCore.QRect(300, 80, 62, 14))
        self.radioButton_Jane.setObjectName("radioButton_Jane")
        self.label_voting_results = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_voting_results.setGeometry(QtCore.QRect(150, 160, 211, 16))
        self.label_voting_results.setText("")
        self.label_voting_results.setObjectName("label_voting_results")
        self.pushButton_vote_candidate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_vote_candidate.setGeometry(QtCore.QRect(150, 130, 181, 20))
        self.pushButton_vote_candidate.setAutoDefault(False)
        self.pushButton_vote_candidate.setObjectName("pushButton_vote_candidate")
        self.label_Please_select = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_Please_select.setGeometry(QtCore.QRect(150, 110, 181, 16))
        self.label_Please_select.setText("")
        self.label_Please_select.setObjectName("label_Please_select")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_vote_menu.setText(_translate("MainWindow", "Vote Menu"))
        self.pushButton_vote.setText(_translate("MainWindow", "Vote"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.radioButton_John.setText(_translate("MainWindow", "John"))
        self.radioButton_Jane.setText(_translate("MainWindow", "Jane"))
        self.pushButton_vote_candidate.setText(_translate("MainWindow", "Vote for selected candidate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())