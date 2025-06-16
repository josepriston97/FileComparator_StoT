# FileComparator_StoT
It is a Python code that analyzes the source data against the target data.


# 📊 Excel File Comparison Tool

This project provides a simple Python-based utility to **compare two Excel files** (source and target) and detect any **row-level differences**. It's especially useful for validating test cases, reports, or verifying data changes between different versions of Excel files.

---

## 🧠 Use Case

This script is intended for:

- Manual QA testers comparing test cases
- Analysts validating updated Excel sheets
- Business users reviewing revisions in data
- ETL or migration checks between Excel exports

---

## ✅ Features

- Compares two Excel files row-by-row
- Checks if **column names match** between source and target
- Identifies **added, removed, or changed rows**
- Outputs differences to both:
  - `differences.xlsx` (Excel format)
  - `differences.txt` (Text format)
- Cleans column names before comparison (lowercased, trimmed)

---

## 🧾 Requirements

- Python 3.7+
- Required libraries:

-bash
pip install pandas openpyxl
🚀 How to Use
Clone the repo or copy the script to your local system.

Update the paths to your Excel files in the script:

source_file = "C:\\Path\\To\\Source.xlsx"
target_file = "C:\\Path\\To\\Target.xlsx"
Run the script:

python compare_excel_files.py
Outputs:

If differences are found:

differences.xlsx: Excel file containing mismatches

differences.txt: Text file with readable output

If no differences:

Message will confirm both files are identical.

📂 File Structure

compare_excel/
│
├── compare_excel_files.py       # Main script
├── differences.xlsx             # (Generated) Excel output of differences
├── differences.txt              # (Generated) Text output of differences
└── README.md                    # Project documentation
🔍 Sample Output
Console Output Example:

Column names are the same between source and target files.
Differences found between source and target data:
<row data shown here>

Differences saved to 'differences.xlsx'.
Differences saved to 'differences.txt'.
🔐 Notes
The script compares exact row matches. If row ordering differs, it may flag differences even if the data is similar.

For large datasets or performance optimization, you may consider hashing or primary key-based joins using merge.

🙌 Author
Name: Jose Priston
Email: josepriston97@gmail.com

📄 License
This project is licensed under the MIT License.


Let me know if you want a **version with CLI support**, logging, or support for **multiple sheets** in a workbook.
