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

import datetime
import pickle

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
	newSendername, newSenderaddress, newReceiver, newObject, newIntroduction, newEnding, newSignature,
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
		self.introduction = newObject
		self.ending = newEnding
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
		"Save an existing lattr object to file"
		f = open(pathToFile, 'wb')
		pickle.dump(self, f)
		f.close()