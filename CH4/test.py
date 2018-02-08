# -*- coding: utf-8 -*-

import re

#
#mySent = 'This book is the best book on Python or M.L. I have evert laid eyes upon.'
#
#regEx = re.compile('\\W*')
#listOfTokens = regEx.split(mySent)
#
#ListOfTokens = [tok.lower() for tok in listOfTokens if len(tok)>0]
#
#print(ListOfTokens)


emailText = open('email/ham/6.txt').read()
regEx = re.compile('\\W*')
listOfTokens = regEx.split(emailText)
print(listOfTokens)