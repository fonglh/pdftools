#!/usr/bin/python3

import PyPDF2
import datetime

# Input consists of 2 files. One has all the front pages.
# The other has all the back pages.
#
# They were stacked in the desired order then fed to the scanner.
# After that, they whole stack was flipped so the reverse side could
# be scanned.

front_file = open('front.pdf', 'rb')
back_file = open('back.pdf', 'rb')
pdf_front = PyPDF2.PdfFileReader(front_file)
pdf_back = PyPDF2.PdfFileReader(back_file)

if pdf_front.numPages != pdf_back.numPages:
    print('The number of front pages does not match the number of back pages.')
    exit(1)

output_file = open('merged.pdf', 'wb')
pdf_writer = PyPDF2.PdfFileWriter()

# Add a front page and a back page to the PDF writer object.
for page_num in range(pdf_front.numPages):
    # Count from the front for the front pages, and count from the back
    # for the back pages.
    front_page = pdf_front.getPage(page_num)
    back_page = pdf_back.getPage(pdf_back.numPages - page_num - 1)
    pdf_writer.addPage(front_page)
    pdf_writer.addPage(back_page)

# Save output PDF to file.
pdf_writer.write(output_file)

front_file.close()
back_file.close()
output_file.close()

