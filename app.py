# -*- coding: utf-8 -*-
#!/bin/env python

__author__ = "el3be"

import docx2pdf
import sys
title = """
    ____  ____  ______
   / __ \/ __ \/ ____/________  ____ _   _____  _____/ /____  _____
  / /_/ / / / / /_  / ___/ __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/
 / ____/ /_/ / __/ / /__/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    
/_/   /_____/_/    \___/\____/_/ /_/|___/\___/_/   \__/\___/_/  

by: el3be@fsociety | Windows 10
------------------------------------------------------------------

"""

def convertir():
	docx = str(input("DOCX file >>> ") + ".docx")
	while docx == ".docx" or docx == " .docx":
		docx = str(input("DOCX file >>> ") + ".docx")
	else:
		pass
	pdf = str(input("PDF file >>> ") + ".pdf")
	while pdf == ".pdf" or pdf == " .pdf":
		pdf = str(input("PDF file >>> ") + ".pdf")
	else:
		pass
	try:
		docx2pdf.convert(docx, pdf)
	except:
		print("An error was ocurred while converting...\nTry again later...")
		sys.exit(0)
def main():
	print(title)
	convertir()
if __name__ == '__main__':
	main()