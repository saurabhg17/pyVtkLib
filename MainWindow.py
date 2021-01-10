from PyQt5 import QtCore, QtWidgets
import sys
import VtkWindow


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setWindowState(QtCore.Qt.WindowMaximized)
		
		self.mVtkWindow = VtkWindow.VtkWindow()
		self.setCentralWidget(self.mVtkWindow)
		
	
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()
