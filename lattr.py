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
	widget.inputSendername.setText(l.sendername)
	widget.inputSenderaddress.setPlainText(l.senderaddress)
	widget.inputReceiver.setPlainText(l.receiver)
	## sentences
	widget.inputObject.setText(l.object)
	widget.inputIntroduction.setText(l.text)
	widget.inputEnding.setText(l.ending)
	widget.inputSignature.setPlainText(l.signature)
	## text
	widget.inputText.setPlainText(l.text)
	# extras
	## packages
	widget.inputPackages.setPlainText(l.packages)
	## attachements
	widget.boolAttachement.setCheckState(l.boolAttachement)
	widget.inputAttachement.setPlainText(l.attachement)

	app.exec_()