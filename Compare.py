import pandas as pd

def compare_excel_files(source_file, target_file):
    # Read Excel files
    source_df = pd.read_excel(source_file, sheet_name=0)
    target_df = pd.read_excel(target_file, sheet_name=0)

    # Clean column names by stripping whitespace and converting to lowercase
    source_df.columns = source_df.columns.str.strip().str.lower()
    target_df.columns = target_df.columns.str.strip().str.lower()

    # Check if the columns are the same in both DataFrames
    if set(source_df.columns) != set(target_df.columns):
        print("Column names are different between source and target files.")
        return
    else:
        print("Column names are the same between source and target files.")

    # Check for row differences
    differences = pd.concat([source_df, target_df]).drop_duplicates(keep=False)

    # If there are any differences
    if not differences.empty:
        print("Differences found between source and target data:")
        print(differences)

        # Overwrite the differences in an Excel file
        differences.to_excel("differences.xlsx", index=False, engine='openpyxl')
        print("\nDifferences saved to 'differences.xlsx'.")

        # Also write the differences in a text file
        with open("differences.txt", "w") as file:
            file.write(differences.to_string(index=False))
        print("\nDifferences saved to 'differences.txt'.")
    else:
        print("\nThe data in the source and target files are identical.")

# Path to your source and target Excel files
source_file = "C:\\LearnPython\\Luma Test Cases - Jose.xlsx"
target_file = "C:\\LearnPython\\Luma Test Cases - Priston.xlsx"

# Run the comparison
compare_excel_files(source_file, target_file)
