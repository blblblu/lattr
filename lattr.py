#!/usr/bin/env python
# lattr - A little application to create letters in LaTeX easily
#
#    Copyright (C) 2011  Sebastian Schulz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
lattr is a program to fetch information from the user (e.g. about the sender, the receiver...).
It creates a *tex file with that information, built with a template.
'''

import sys, locale
from PyQt4 import QtCore, QtGui, uic
import pickle
from lattrlib import *

class LattrMainWindow(QtGui.QMainWindow):
	"Class for the lattr main window"
	def __init__(self, *args):
		QtGui.QWidget.__init__(self, *args)
		uic.loadUi("ui/lattr.ui", self)
		self.actionOpen.triggered.connect(self.openFileUi)
		self.actionSaveAs.triggered.connect(self.saveLattrToFileUi)
		self.actionExportAsTex.triggered.connect(self.saveLattrAsTexUi)
		self.actionAbout.triggered.connect(self.showAboutWindow)

	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, 'Quit application?',
			("Are you sure to quit?"), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def setUiData(self, lattr):
		"set forms to values of a given lattr object"
		# document settings
		## document
		self.inputTemplate.setText(lattr.template)
		self.inputFontsize.setValue(lattr.fontsize)
		self.inputLanguage.setText(lattr.language)
		self.inputAlign.setCurrentIndex(lattr.align)
		## time
		self.inputDate.setDate(lattr.date)
		# content
		## addresses
		self.inputSendername.setText(lattr.sendername)
		self.inputSenderaddress.setPlainText(lattr.senderaddress)
		self.inputReceiver.setPlainText(lattr.receiver)
		## sentences
		self.inputObject.setText(lattr.object)
		self.inputOpening.setText(lattr.opening)
		self.inputClosing.setText(lattr.closing)
		self.inputSignature.setPlainText(lattr.signature)
		## text
		self.inputText.setPlainText(lattr.text)
		# extras
		## packages
		self.inputPackages.setPlainText(lattr.packages)
		## attachements
		self.boolAttachement.setCheckState(lattr.boolAttachement)
		self.inputAttachement.setPlainText(lattr.attachement)

	def getUiData(self):
		"Returns a lattr object containing the current information"
		l = lattr()
		# document settings
		## document
		l.template = self.inputTemplate.text()
		l.fontsize = self.inputFontsize.value()
		l.language = self.inputLanguage.text()
		l.align = self.inputAlign.currentIndex()
		## time
		l.date = self.inputDate.date()
		# content
		## addresses
		l.sendername = self.inputSendername.text()
		l.senderaddress = self.inputSenderaddress.toPlainText()
		l.receiver = self.inputReceiver.toPlainText()
		## sentences
		l.object = self.inputObject.text()
		l.opening = self.inputOpening.text()
		l.closing = self.inputClosing.text()
		l.signature = self.inputSignature.toPlainText()
		## text
		l.text = self.inputText.toPlainText()
		# extras
		## packages
		l.packages = self.inputPackages.toPlainText()
		## attachements
		l.boolAttachement = self.boolAttachement.checkState()
		l.attachement = self.inputAttachement.toPlainText()
		return l


	def openFileUi(self):
		"Opens a file dialog to open an existing document"
		pathToFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '', '*.lattr')
		openedFile = open(pathToFile, 'rb')
		openedLattr = pickle.load(openedFile)
		openedFile.close()
		self.setUiData(openedLattr)

	def saveLattrToFileUi(self):
		"Opens a file dialog to save the current document"
		pathToFile = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', '*.lattr')
		l = self.getUiData()
		l.saveLattrToFile(pathToFile)

	def saveLattrAsTexUi(self):
		"Opens a file dialog to save the current document as *.tex file"
		pathToFile = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '', '*.tex')
		l = self.getUiData()
		l.saveLattrAsTex(pathToFile)

	def showAboutWindow(self):
		"Opens an about window"
		widget = LattrAboutWindow()
		widget.exec()

	#@QtCore.pyqtSignature("")

class LattrAboutWindow(QtGui.QDialog):
	"Class for the lattr about window"
	def __init__(self, *args):
		QtGui.QWidget.__init__(self, *args)
		uic.loadUi("ui/about.ui", self)

def main(args):
	app = QtGui.QApplication(args)
	translator = QtCore.QTranslator(app)
	translator.load("lattr_"+locale.getlocale()[0]+".qm")
	app.installTranslator(translator)
	widget = LattrMainWindow()
	widget.show()
	# lattr instance for current letter
	l = lattr()
	widget.setUiData(l)
	
	app.exec_()

if __name__ == '__main__':
	main(sys.argv)