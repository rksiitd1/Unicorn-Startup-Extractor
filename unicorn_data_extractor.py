import pandas as pd
from bs4 import BeautifulSoup
import os

# Get input file path from user
input_file = input("Enter the path to the HTML file: ")

# Open the local HTML file
with open(input_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

data = []
companies = soup.find_all('h3')

for i, company in enumerate(companies):
    company_data = {}
    company_data["S.N."] = i + 1
    company_data["Name"] = company.text.strip()

    details_ul = company.find_next_sibling('ul')
    if details_ul:
        details = details_ul.find_all('li')
        for detail in details:
            parts = detail.text.strip().split(':')
            if len(parts) >= 2:
                key = parts[0].strip()
                value = ':'.join(parts[1:]).strip()
                company_data[key] = value

    data.append(company_data)

df = pd.DataFrame(data)

# Get output file name from user
output_filename = input("Enter the desired output Excel file name (without extension): ")

# Get the directory of the input file
output_dir = os.path.dirname(input_file)

# Construct the full output file path
output_file = os.path.join(output_dir, output_filename + ".xlsx")

# Export to Excel
df.to_excel(output_file, index=False)

print(f"Data extracted and saved to {output_file}")