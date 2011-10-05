#!/usr/bin/env python
# lattr - A little application to create letters in LaTeX easily

'''
lattr is a program to fetch information from the user (e.g. about the sender, the receiver...).
It creates a *tex file with that information, built with a template.
'''

import sys
from PyQt4 import QtCore, QtGui, uic
from lattrlib import *

class LattrMainWindow(QtGui.QMainWindow):
	"Class for the lattr main window"
	def __init__(self, *args):
		QtGui.QWidget.__init__(self, *args)
		uic.loadUi("ui/lattr.ui", self)

	#@QtCore.pyqtSignature("")

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	widget = LattrMainWindow()
	widget.show()
	# lattr instance for current letter
	l = lattr()
	# set forms to defaults
	# document settings
	## document
	widget.inputTemplate.setText(l.template)
	widget.inputFontsize.setValue(l.fontsize)
	widget.inputLanguage.setText(l.language)
	widget.inputAlign.setCurrentIndex(l.align)
	## time
	widget.inputDate.setDate(l.date)
	# content
	## addresses
	# TODO: change all setText() of QPlainTextEdit to setDocument() and correct arguments
	widget.inputSendername.setText(l.sendername)
	widget.inputSenderaddress.setDocument(l.senderaddress)
	widget.inputReceiver.setText(l.receiver)
	## sentences
	widget.inputObject.setText(l.object)
	widget.inputIntroduction.setText(l.text)
	widget.inputEnding.setText(l.ending)
	widget.inputSignature.setText(l.signature)
	## text
	widget.inputText.setText(l.text)
	# extras
	## packages
	widget.inputPackages.setText(l.packages)
	## attachements
	widget.boolAttachement.setCheckState(True)
	widget.inputAttachements.setText(l.attachements)

	app.exec_()