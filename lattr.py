#!/usr/bin/env python
# lattr - A little application to create letters in LaTeX easily

'''
lattr is a program to fetch information from the user (e.g. about the sender, the receiver...).
It creates a *tex file with that information, built with a template
'''

import sys
from PyQt4 import QtCore, QtGui, uic

class LattrMainWindow(QtGui.QMainWindow):
	"Class for the lattr main window"
	def __init__(self, *args):
		QtGui.QWidget.__init__(self, *args)
		uic.loadUi("lattr.ui", self)

	#@QtCore.pyqtSignature("")

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	widget = LattrMainWindow()
	widget.show()
	print(widget)
	app.exec_()
		