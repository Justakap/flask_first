import re
from prettytable import PrettyTable
from PyPDF2 import PdfReader

reader = PdfReader("pdf/CS_Syllabus.pdf")
page = reader.pages[35]
text = page.extract_text()

print(text)

