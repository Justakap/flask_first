from prettytable import PrettyTable
import re
from PyPDF2 import PdfReader
import json
# reader = PdfReader("pdf/22eskcs020.pdf")
# page = reader.pages[0]
# text = page.extract_text()
text = """RAJASTHAN  TECHNICAL  UNIVERSITY
KOTA
B. Tech  II  SEM  MAIN  EXAM   2025  (GRADING)
(Powered by www.rtu.ac.in)
College Name: SWAMI KESHVANAND INSTITUTE OF TECHNOLOGY, MANAGEMENT & GRAMOTHAN, JAIPUR
Roll No : 24ESKCS450 Enrollment No : 24E1SKCSM40P450
Name : ANANT KHANDELWAL Father's Name : abc
COURSE TITLE COURSE CODE MARKS1(MIDTERM) MARKS2(ENDTERM) GRADE
Human Values 2FY1-05 25 63 A++
Human Values Activities And Sports 2FY1-23 54 40 A++
Engineering Mathematics-II 2FY2-01 22 61 A
Engineering Chemistry 2FY2-03 25 58 A++
Engineering Chemistry Lab 2FY2-21 48 36 A
Basic Mechanical Engineering 2FY3-07 27 52 A+
Basic Civil Engineering 2FY3-09 27 41 B+
Manufacturing Practices Workshop 2FY3-25 51 32 A
Basic Civil Engineering Lab 2FY3-27 49 35 A++
Computer Aided Machine Drawing 2FY3-29 51 34 A
Sodeca 2FY8-00 95 A++
REMARKS : PASS
Instruction :
1. This is web based result. Authentic result shall be considered in mark-sheet issued by RTU.
2. The due date to submit an online copy view and revaluation form through the college is FIFTEEN days after the date results are announced.
3 Students can apply copy view for all the theory subjects. The revaluation is permitted in maximum FOUR theory papers.
4.Student can apply for view his/her answer book(Copy View) simultaneously with revaluation of answer book in same subject.
5.After inspection of answer book(S) , offline (Manual) revaluation application form will not be accepted.  
6. Candidates applying for inspection of answer-books are also required to apply simultaneously for Revaluation before last
date as announced by the University."""

roll_no_pattern = r"Roll No\s*:\s*(\w+)"
roll_no_match = re.search(roll_no_pattern, text)
roll_no = roll_no_match.group(1) if roll_no_match else ''

remark_pattern = r"REMARKS\s*:\s*(\w+)"
remark_match = re.search(remark_pattern, text)
remark = remark_match.group(1) if remark_match else ''

name_pattern = r"Name\s*:\s*(.*)\s*Father's Name"
name_match = re.search(name_pattern, text)
name = name_match.group(1).strip() if name_match else ''

pattern = r"(.+?) (\w+-\d+) (\d+) (\d+) (\w+\+*)"
matches = re.findall(pattern, text)

table_data = [{'Subject Name': match[0], 'Subject Code': match[1],
               'Internal Marks': match[2], 'External Marks': match[3],
               'Total Marks': int(match[2]) + int(match[3]), 'Grade': match[4]} for match in matches]

table_data = sorted(table_data, key=lambda x: x['Total Marks'], reverse=True)

table = PrettyTable()
table.field_names = ["Subject Name", "Subject Code",
                     "Internal Marks", "External Marks", "Total Marks", "Grade"]

for row in table_data:
    table.add_row([row['Subject Name'], row['Subject Code'], row['Internal Marks'], row['External Marks'],
                   row['Total Marks'], row['Grade']])

final_marks = sum(row['Total Marks'] for row in table_data)
total_rows = len(table_data)


data = {
    "Name": name,
    "Roll No": roll_no,
    "Result": remark,
    "Percentage": final_marks / total_rows,
    "Subjects": table_data
}

json_data = json.dumps(data, indent=4)

# Print JSON data
print(json_data)
# print(text)

# print("Name : ", name)
# print("Roll No : ", roll_no)
# print("Result : ", remark)
# print("Percentage : " + str(final_marks/total_rows) + "%")
# print(table)
