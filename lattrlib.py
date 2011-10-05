#!/usr/bin/env python
# lattrlib - library for lattr

'''
This file contains all lattr specific functions, e.g. modifying the template.
It also contains the default values for the letter.
'''

import datetime

# variables for text align
align_block = 0
align_left = 1
align_right = 2

class lattr(object):
	"the lattr class"
	def __init__(self):
		super(lattr, self).__init__()
		# document settings
		## document
		self.template = 'scrlttr2'
		self.fontsize = 10.0
		self.language = 'ngerman'
		self.align = align_block
		## time
		self.date = datetime.date.today()
		# content
		## addresses
		self.sendername = ''
		self.senderaddress = ''
		self.receiver = ''
		## sentences
		self.object = ''
		self.introduction = ''
		self.ending = ''
		self.signature = ''
		## text
		self.text = ''
		# extras
		## packages
		self.packages = ''
		## attachements
		self.boolAttachement = False
		self.attachements = ''