# Your Python code goes here
# excercise 8 
# # write a program to manipute pdf files ising pyPDF . 
# your programs should be able to merge multiple pdf files into a single pdf.
#  you are welcome to add more functionalities 
# pypdf is a free and open -source -pure-python pdf library capable of splitio, merging, 
#   cropping and transforming the pages of pdf files, it casn a aslo add coustom data , viewing options
# and passwords to pdf files . pypdf can retrive text aand metadata from pdfs as well

import PyPDF2
#  to read the pdf
with open('sample.pdf','rb')as file :
     reader= PyPDF2.PdfReader(file )
     
     num_pages =len(reader.pages)
     print(f" Total number of pages : {num_pages}")
     
     for page_num in range (num_pages):
         page= reader.pages[page_num]
         text = page.extract_text()
         print(f"Page {page_num + 1 } content:\n {text }")
         
    
    
#  for merging the  pdf files 

pdfs=['file1.pdf','file2.pdf','file3.pdf']   
merger = PyPDF2.PdfFileWriter()
for pdf in  pdfs:
    with open('sample.pdf','rb')as file :
        reader= PyPDF2.PdfReader(file )
        for page_num in range(len(reader.pages)):
            
            merger.add_page(reader.pages[page_num])
with  open ( 'merged.odf','wb') as output_file:
    merger.write(output_file)