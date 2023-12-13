# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setMinimumSize(QtCore.QSize(400, 650))
        MainWindow.setMaximumSize(QtCore.QSize(400, 650))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outputLabel = QtWidgets.QLabel(self.frame)
        self.outputLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.outputLabel.setStyleSheet("font: 87 40pt \"Arial Black\";\n"
"background-color:#000;\n"
"color: #fff;\n"
"\n"
"\n"
"")
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.verticalLayout.addWidget(self.outputLabel)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clearButton = QtWidgets.QPushButton(self.frame_6)
        self.clearButton.setMaximumSize(QtCore.QSize(130, 130))
        self.clearButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_6.addWidget(self.clearButton)
        self.percentageButton = QtWidgets.QPushButton(self.frame_6)
        self.percentageButton.setMaximumSize(QtCore.QSize(130, 130))
        self.percentageButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.percentageButton.setObjectName("percentageButton")
        self.horizontalLayout_6.addWidget(self.percentageButton)
        self.backspaceButton = QtWidgets.QPushButton(self.frame_6)
        self.backspaceButton.setMaximumSize(QtCore.QSize(130, 130))
        self.backspaceButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.backspaceButton.setObjectName("backspaceButton")
        self.horizontalLayout_6.addWidget(self.backspaceButton)
        self.divisionButton = QtWidgets.QPushButton(self.frame_6)
        self.divisionButton.setMaximumSize(QtCore.QSize(130, 130))
        self.divisionButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.divisionButton.setObjectName("divisionButton")
        self.horizontalLayout_6.addWidget(self.divisionButton)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sevenButton = QtWidgets.QPushButton(self.frame_5)
        self.sevenButton.setMaximumSize(QtCore.QSize(130, 130))
        self.sevenButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.sevenButton.setObjectName("sevenButton")
        self.horizontalLayout_4.addWidget(self.sevenButton)
        self.eighButton = QtWidgets.QPushButton(self.frame_5)
        self.eighButton.setMaximumSize(QtCore.QSize(130, 130))
        self.eighButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.eighButton.setObjectName("eighButton")
        self.horizontalLayout_4.addWidget(self.eighButton)
        self.nineButton = QtWidgets.QPushButton(self.frame_5)
        self.nineButton.setMaximumSize(QtCore.QSize(130, 130))
        self.nineButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.nineButton.setObjectName("nineButton")
        self.horizontalLayout_4.addWidget(self.nineButton)
        self.multiplicationButton = QtWidgets.QPushButton(self.frame_5)
        self.multiplicationButton.setMaximumSize(QtCore.QSize(130, 130))
        self.multiplicationButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.multiplicationButton.setObjectName("multiplicationButton")
        self.horizontalLayout_4.addWidget(self.multiplicationButton)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fourButton = QtWidgets.QPushButton(self.frame_4)
        self.fourButton.setMaximumSize(QtCore.QSize(130, 130))
        self.fourButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.fourButton.setObjectName("fourButton")
        self.horizontalLayout_5.addWidget(self.fourButton)
        self.fiveButton = QtWidgets.QPushButton(self.frame_4)
        self.fiveButton.setMaximumSize(QtCore.QSize(130, 130))
        self.fiveButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.fiveButton.setObjectName("fiveButton")
        self.horizontalLayout_5.addWidget(self.fiveButton)
        self.sixButton = QtWidgets.QPushButton(self.frame_4)
        self.sixButton.setMaximumSize(QtCore.QSize(130, 130))
        self.sixButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.sixButton.setObjectName("sixButton")
        self.horizontalLayout_5.addWidget(self.sixButton)
        self.subtractionButton = QtWidgets.QPushButton(self.frame_4)
        self.subtractionButton.setMaximumSize(QtCore.QSize(130, 130))
        self.subtractionButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.subtractionButton.setObjectName("subtractionButton")
        self.horizontalLayout_5.addWidget(self.subtractionButton)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.oneButton = QtWidgets.QPushButton(self.frame_3)
        self.oneButton.setMaximumSize(QtCore.QSize(130, 130))
        self.oneButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.oneButton.setObjectName("oneButton")
        self.horizontalLayout_3.addWidget(self.oneButton)
        self.twoButton_9 = QtWidgets.QPushButton(self.frame_3)
        self.twoButton_9.setMaximumSize(QtCore.QSize(130, 130))
        self.twoButton_9.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.twoButton_9.setObjectName("twoButton_9")
        self.horizontalLayout_3.addWidget(self.twoButton_9)
        self.threeButton = QtWidgets.QPushButton(self.frame_3)
        self.threeButton.setMaximumSize(QtCore.QSize(130, 130))
        self.threeButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.threeButton.setObjectName("threeButton")
        self.horizontalLayout_3.addWidget(self.threeButton)
        self.addictionButton = QtWidgets.QPushButton(self.frame_3)
        self.addictionButton.setMaximumSize(QtCore.QSize(130, 130))
        self.addictionButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.addictionButton.setObjectName("addictionButton")
        self.horizontalLayout_3.addWidget(self.addictionButton)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zeroButton = QtWidgets.QPushButton(self.frame_2)
        self.zeroButton.setMaximumSize(QtCore.QSize(130, 130))
        self.zeroButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.zeroButton.setObjectName("zeroButton")
        self.horizontalLayout_2.addWidget(self.zeroButton)
        self.moreorlessButton = QtWidgets.QPushButton(self.frame_2)
        self.moreorlessButton.setMaximumSize(QtCore.QSize(130, 130))
        self.moreorlessButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.moreorlessButton.setObjectName("moreorlessButton")
        self.horizontalLayout_2.addWidget(self.moreorlessButton)
        self.pointButton = QtWidgets.QPushButton(self.frame_2)
        self.pointButton.setMaximumSize(QtCore.QSize(130, 130))
        self.pointButton.setObjectName("pointButton")
        self.horizontalLayout_2.addWidget(self.pointButton)
        self.equalButton = QtWidgets.QPushButton(self.frame_2)
        self.equalButton.setMaximumSize(QtCore.QSize(130, 130))
        self.equalButton.setStyleSheet("\n"
"font: 87 36pt \"Arial Black\";")
        self.equalButton.setObjectName("equalButton")
        self.horizontalLayout_2.addWidget(self.equalButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CalculadoraPython"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.clearButton.setText(_translate("MainWindow", "AC"))
        self.percentageButton.setText(_translate("MainWindow", "%"))
        self.backspaceButton.setText(_translate("MainWindow", "<<"))
        self.divisionButton.setText(_translate("MainWindow", "/"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eighButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.multiplicationButton.setText(_translate("MainWindow", "*"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.subtractionButton.setText(_translate("MainWindow", "-"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton_9.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.addictionButton.setText(_translate("MainWindow", "+"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.moreorlessButton.setText(_translate("MainWindow", "+/-"))
        self.pointButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
