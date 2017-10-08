import PyPDF2
import datetime

# Input is a single PDF file which has 1 page for each month, arranged
# in descending chronological order.

input_file = open('statement.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(input_file)

# Define the year and month of the first page here.
year = 2016
month = 4

for page_num in range(pdf_reader.numPages):
    # Figure out filename and create a new PdfFileWriter object.
    date = datetime.date(year, month, 1)
    output_file = open(date.strftime('%Y%m') + '-statement.pdf', 'wb')
    pdf_writer = PyPDF2.PdfFileWriter()

    # Write 1 page to its own file.
    page = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page)
    pdf_writer.write(output_file)
    output_file.close()

    # Go to the previous month.
    month -= 1
    if month == 0:
        month = 12
        year -= 1

input_file.close()

