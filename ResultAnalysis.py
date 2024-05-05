from prettytable import PrettyTable
import re
from PyPDF2 import PdfReader

reader = PdfReader("pdf/21eskcs058 (1).pdf")
page = reader.pages[0]
text = page.extract_text()


roll_no_pattern = r"Roll No\s*:\s*(\w+)"
roll_no_match = re.search(roll_no_pattern, text)
roll_no = roll_no_match.group(1) if roll_no_match else ''

remark_pattern = r"REMARKS\s*:\s*(\w+)"
remark_match = re.search(remark_pattern, text)
remark = remark_match.group(1) if remark_match else ''

name_pattern = r"Name\s*:\s*(.*)\s*Father's Name"
name_match = re.search(name_pattern, text)
name = name_match.group(1).strip() if name_match else ''

sem_name_pattern = r"B. Tech\s*(.*)\s*"
sem_name_match = re.search(sem_name_pattern, text)
sem_name = sem_name_match.group(1).strip() if sem_name_match else ''


father_name_pattern = r"Father's Name\s*:\s*(.*)\s*"
father_name_pattern = re.search(father_name_pattern, text)
father_name = father_name_pattern.group(
    1).strip() if father_name_pattern else ''


College_name_pattern = r"College Name\s*:\s*(.*)\s*"
College_name_pattern = re.search(College_name_pattern, text)
College_name = College_name_pattern.group(
    1).strip() if College_name_pattern else ''

Sodeca_name_pattern = r"SODECA (\w+-\d+) (\d+) (\w\++)"
matches = re.findall(Sodeca_name_pattern, text)
sodeca_data = [{'Sodeca_Code': match1[0], 'Sodeca_EndTerm': match1[1],
                "Grade:": match1[2]} for match1 in matches]

pattern = r"(.+?) (\w+-\d+) (\d+) (\d+) (\w+\+*)"

matches = re.findall(pattern, text) 

table_data = [{'Subject_Name': match[0], 'Subject_Code': match[1],
               'Internal_Marks': int(match[2]), 'External_Marks': int(match[3]),
               'Total_Marks': int(match[2]) + int(match[3]), 'Grade': match[4]} for match in matches]


table = PrettyTable()
table.field_names = ["Subject Name", "Subject Code",
                     "Internal Marks", "External Marks", "Total Marks", "Grade"]

for row in table_data:
    table.add_row([row['Subject_Name'], row['Subject_Code'], row['Internal_Marks'], row['External_Marks'],
                   row['Total_Marks'], row['Grade']])

final_marks = sum(row['Total_Marks'] for row in table_data)


# print(table)
