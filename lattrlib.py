#!/usr/bin/env python
#    lattrlib - library for lattr
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

def rawString(string):
	"Like repr(), but without the first and last character"
	return(repr(string)[1:-1])

def buildDvi(pathToTex):
	"Runs LaTeX and opens a saved *.tex file"
	os.chdir(re.sub(r'[^/]*$', '', pathToTex))
	return os.system('latex '+pathToTex)

def buildPdf(pathToTex):
	"Runs pdflatex and opens a saved *.tex file"
	os.chdir(re.sub(r'[^/]*$', '', pathToTex))
	return os.system('pdflatex '+pathToTex)

class lattr(object):
	"The lattr class"
	def __init__(self):
		super(lattr, self).__init__()

		# set data to defaults
		self.setData('scrlttr2', 10, 'ngerman', align_block, datetime.date.today(), '', '', '', '', '', '', '', '', '', False, '')

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

	def saveLattrAsTex(self, templateDir, pathToFile):
		'''
		Saves lattr object as *.tex file
		Returns 0 if it worked
		'''
		try:
			templateFile = open(templateDir+self.template+'/template.tex', 'r')
			letter = templateFile.read()
			templateFile.close()
			# document settings
			## document
			letter = re.sub(r'%<fontsize>', str(self.fontsize), letter)
			letter = re.sub(r'%<language>', rawString(self.language), letter)
			if self.align == align_left:
				letter = re.sub(r'%<align>', '\\\\flushleft', letter)
			if self.align == align_right:
				letter = re.sub(r'%<align>', '\\\\flushright', letter)
			## time
			letter = re.sub(r'%<date>', self.date.toString(), letter)
			# content
			## addresses
			letter = re.sub(r'%<sendername>', rawString(self.sendername), letter)
			letter = re.sub(r'%<senderaddress>', rawString(self.senderaddress), letter)
			letter = re.sub(r'%<receiver>', rawString(self.receiver), letter)
			## sentences
			letter = re.sub(r'%<object>', rawString(self.object), letter)
			letter = re.sub(r'%<opening>', rawString(self.opening), letter)
			letter = re.sub(r'%<closing>', rawString(self.closing), letter)
			letter = re.sub(r'%<signature>', rawString(self.signature), letter)
			## text
			letter = re.sub(r'%<text>', rawString(self.text), letter)
			# extras
			## packages
			letter = re.sub(r'%<packages>', rawString(self.packages), letter)
			## attachements
			if self.boolAttachement:
				letter = re.sub(r'%<boolAttachement>', '', letter)
			else:
				letter = re.sub(r'%<boolAttachement>', '%', letter)
			letter = re.sub(r'%<attachement>', rawString(self.attachement), letter)
		except IOError:
			return 1
		try:
			f = open(pathToFile, 'w')
			f.write(letter)
			f.close()
			return 0
		except IOError:
			return 2