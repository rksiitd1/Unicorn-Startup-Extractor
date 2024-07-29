# Unicorn Startup Data Extractor

This Python script extracts detailed information about unicorn startups from a locally saved HTML file. It's designed to work with web pages that list unicorn companies and their details in a specific format. The script parses the HTML, extracts relevant data, and exports it to an Excel spreadsheet for easy analysis.

## Features

- Extracts data from a locally saved HTML file
- Parses company names and detailed information
- Organizes data into a structured format
- Exports data to an Excel spreadsheet
- User-friendly input for file paths and names
- Saves the output file in the same directory as the input file

## Requirements

- Python 3.x
- Required Python libraries:
  - pandas
  - beautifulsoup4

You can install the required libraries using pip:

```bash
pip install pandas beautifulsoup4
```

## Usage

1. Save the HTML content of the unicorn startup listing page to a local file.

2. Run the script:
   ```bash
   python unicorn_data_extractor.py
   ```

3. When prompted, enter the path to your saved HTML file.

4. Enter a name for the output Excel file (without the .xlsx extension).

5. The script will process the HTML file and create an Excel spreadsheet in the same directory as the input file.

## How It Works

1. **HTML Parsing**: The script uses BeautifulSoup to parse the HTML content of the input file.

2. **Data Extraction**: 
   - Company names are extracted from `<h3>` tags.
   - Company details are extracted from `<li>` elements within `<ul>` tags following each company name.

3. **Data Structure**: The script creates a list of dictionaries, where each dictionary represents a company and its details.

4. **Data Processing**: 
   - A serial number (S.N.) is added to each company entry.
   - Company details are split into key-value pairs.

5. **DataFrame Creation**: The extracted data is converted into a pandas DataFrame.

6. **Excel Export**: The DataFrame is exported to an Excel file using pandas' `to_excel` function.

## Code Explanation

```python
import pandas as pd
from bs4 import BeautifulSoup
import os

# Get input file path from user
input_file = input("Enter the path to the HTML file: ")

# Open and read the HTML file
with open(input_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize data list
data = []

# Find all company names (assumed to be in <h3> tags)
companies = soup.find_all('h3')

# Extract data for each company
for i, company in enumerate(companies):
    company_data = {"S.N.": i + 1, "Name": company.text.strip()}
    
    # Find the <ul> tag containing company details
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

# Create DataFrame
df = pd.DataFrame(data)

# Get output file name from user
output_filename = input("Enter the desired output Excel file name (without extension): ")

# Construct output file path
output_dir = os.path.dirname(input_file)
output_file = os.path.join(output_dir, output_filename + ".xlsx")

# Export to Excel
df.to_excel(output_file, index=False)

print(f"Data extracted and saved to {output_file}")
```

## Notes

- This script assumes a specific HTML structure where company names are in `<h3>` tags and details are in `<li>` elements within `<ul>` tags immediately following each company name.
- The script may need adjustments if the HTML structure of the source page changes.
- Ensure you have the necessary permissions to read the input file and write to the output directory.

## Contributing

Contributions to improve the script are welcome. Please feel free to submit a pull request or open an issue on GitHub.

## License

MIT License

Copyright (c) 2023 Ratnesh Kumar Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author

Ratnesh Kumar Sharma (GitHub: [@rksiitd](https://github.com/rksiitd))

---

For any questions or issues, please open an issue on the GitHub repository.
