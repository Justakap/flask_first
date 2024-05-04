from prettytable import PrettyTable
import re
from PyPDF2 import PdfReader
import json
reader = PdfReader("pdf/22eskit143.pdf")
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

# print("Name : ", name)
# print("Roll No : ", roll_no)
# print("Result : ", remark)
# print("Percentage : " + str(final_marks/total_rows) + "%")
# print(table)
