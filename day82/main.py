# Your Python code goes here
#  merge the pdf
from PyPDF2 import PdfWriter
import os 
merger =PdfWriter()
files=[ file for file in os.listdir() if file.endswith('.pdf')]
for pdf in ['file1.pdf','file2.pdf','file3.pdf']:
    merger.append(pdf)
    
merger.wrtie('merged-pdf.pdf')
merger.close()