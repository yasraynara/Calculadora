import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from tela import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.zeroButton.clicked.connect(lambda: pressionado("0"))
        self.ui.oneButton.clicked.connect(lambda: pressionado("1"))
        self.ui.twoButton_9.clicked.connect(lambda: pressionado("2"))
        self.ui.threeButton.clicked.connect(lambda: pressionado("3"))
        self.ui.fourButton.clicked.connect(lambda: pressionado("4"))
        self.ui.fiveButton.clicked.connect(lambda: pressionado("5"))
        self.ui.sixButton.clicked.connect(lambda: pressionado("6"))
        self.ui.sevenButton.clicked.connect(lambda: pressionado("7"))
        self.ui.eighButton.clicked.connect(lambda: pressionado("8"))
        self.ui.nineButton.clicked.connect(lambda: pressionado("9"))
        self.ui.pointButton.clicked.connect(lambda: pressionado("."))
        self.ui.addictionButton.clicked.connect(lambda: pressionado("+"))
        self.ui.subtractionButton.clicked.connect(lambda: pressionado("-"))
        self.ui.divisionButton.clicked.connect(lambda: pressionado("/"))
        self.ui.multiplicationButton.clicked.connect(lambda: pressionado("*"))
        self.ui.equalButton.clicked.connect(lambda: resultado())
        self.ui.clearButton.clicked.connect(lambda: clearOutput())
        self.ui.backspaceButton.clicked.connect(lambda: backspace())

        def resultado():
            saida = self.ui.outputLabel.text()
            try:
                resposta = eval(saida)
                self.ui.outputLabel.setText(f"{resposta:.1f}")
            except:
                self.ui.outputLabel.setText("ERRO")

        def backspace():
            saida = self.ui.outputLabel.text()
            self.ui.outputLabel.setText(saida[:-1])
            if not len(saida[:-1]):
                clearOutput()

        def clearOutput():
            self.ui.outputLabel.setText("0")

        self.operacoes = ['+', '-', '*', '/', '.']

        def pressionado(tecla):
            saida = self.ui.outputLabel.text()
            if saida == "0":
                saida = ""
            if tecla in self.operacoes and saida[-1] in self.operacoes:
                saida = saida[:-1]
            saida += tecla
            self.ui.outputLabel.setText(saida)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())