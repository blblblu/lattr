#!/usr/bin/env python
# lattrlib - library for lattr
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
This file contains all lattr specific functions, e.g. modifying the template.
It also contains the default values for the letter.
'''

import os
import datetime
import pickle
import re

# variables for text align
align_block = 0
align_left = 1
align_right = 2

class lattr(object):
	"The lattr class"
	def __init__(self):
		super(lattr, self).__init__()

		# set data to defaults
		self.setData('scrlttr2', 10.0, 'ngerman', align_block, datetime.date.today(), '', '', '', '', '', '', '', '', '', False, '')

	def setData(self,
	# document settings
	newTemplate, newFontsize, newLanguage, newAlign, newDate,
	# content
	newSendername, newSenderaddress, newReceiver, newObject, newOpening, newClosing, newSignature,
	newText,
	# extras
	newPackages, newBoolAttachement, newAttachement):
		"Function for setting the whole letter at once"
		# document settings
		## document
		self.template = newTemplate
		self.fontsize = newFontsize
		self.language = newLanguage
		self.align = newAlign
		## time
		self.date = newDate
		# content
		## addresses
		self.sendername = newSendername
		self.senderaddress = newSenderaddress
		self.receiver = newReceiver
		## sentences
		self.object = newObject
		self.opening = newOpening
		self.closing = newClosing
		self.signature = newSignature
		## text
		self.text = newText
		# extras
		## packages
		self.packages = newPackages
		## attachements
		self.boolAttachement = newBoolAttachement
		self.attachement = newAttachement

	def saveLattrToFile(self, pathToFile):
		"Saves lattr object to file"
		f = open(pathToFile, 'wb')
		pickle.dump(self, f)
		f.close()

	def saveLattrAsTex(self, pathToFile):
		"Saves lattr object as *.tex file"
		templateFile = open(os.getcwd()+'/templates/'+self.template+'/template.tex', 'r')
		letter = templateFile.read()
		templateFile.close()
		# document settings
		## document
		letter = re.sub(r'%<fontsize>', str(self.fontsize), letter)
		letter = re.sub(r'%<language>', self.language, letter)
		#letter = re.sub(r'%<align>', self.align, letter)
		## time
		letter = re.sub(r'%<date>', self.date.toString(), letter)
		# content
		## addresses
		letter = re.sub(r'%<sendername>', self.sendername, letter)
		letter = re.sub(r'%<senderaddress>', self.senderaddress, letter)
		letter = re.sub(r'%<receiver>', self.receiver, letter)
		## sentences
		letter = re.sub(r'%<object>', self.object, letter)
		letter = re.sub(r'%<opening>', self.opening, letter)
		letter = re.sub(r'%<closing>', self.closing, letter)
		letter = re.sub(r'%<signature>', self.signature, letter)
		## text
		letter = re.sub(r'%<text>', self.text, letter)
		# extras
		## packages
		letter = re.sub(r'%<packages>', self.packages, letter)
		## attachements
		if self.boolAttachement:
			letter = re.sub(r'%<boolAttachement>', '', letter)
		else:
			letter = re.sub(r'%<boolAttachement>', '%', letter)
		letter = re.sub(r'%<attachement>', self.attachement, letter)
		f = open(pathToFile, 'w')
		f.write(letter)
		f.close()