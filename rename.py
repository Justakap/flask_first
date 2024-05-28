import os
import re
import PyPDF2
from PyPDF2 import PdfReader


def extract_roll_no_from_pdf(file_path):
    roll_no_pattern = r"Roll No\s*:\s*(\w+)"
    try:
        with open(file_path, "rb") as file:
            reader = PdfReader(file)
            if 1 > 0:
                page = reader.pages[0]
                text = page.extract_text()

                roll_no_match = re.search(roll_no_pattern, text)
                if roll_no_match:
                    return roll_no_match.group(1)
                else:
                    print(f"No roll number found in {file_path}")
                    return None
            else:
                print(f"No pages found in {file_path}")
                return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def rename_files_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            current_file_path = os.path.join(folder_path, filename)

            if os.path.isfile(current_file_path) and filename.lower().endswith(".pdf"):
                roll_no = extract_roll_no_from_pdf(current_file_path)
                if roll_no:
                    new_file_path = os.path.join(folder_path, f"{roll_no}.pdf")
                    os.rename(current_file_path, new_file_path)
                    print(f"Renamed '{filename}' to '{roll_no}.pdf'")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    # Prompt the user for the folder path
    folder_path = input("Enter the path to the folder containing the PDF files: ")
    rename_files_in_folder(folder_path)


if __name__ == "__main__":
    main()
