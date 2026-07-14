import pandas as pd
import csv
import re

# ==========================================
# LOAD DATA
# ==========================================

print("Loading Product Dataset...")

df = pd.read_csv(
    "data/Product_return_fake_detection.csv",
    encoding="utf-8"
)

print("Dataset Loaded Successfully")
print()

# Remove hidden spaces from column names
df.columns = df.columns.str.strip()

print("Columns Found:")
print(df.columns.tolist())
print()

# ==========================================
# REMOVE UNNAMED COLUMNS
# ==========================================

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# ==========================================
# CLEAN ALL TEXT COLUMNS
# ==========================================

print("Cleaning Text Columns...")

def clean_text(text):

    text = str(text)

    # remove all newline variations
    text = re.sub(r'[\r\n]+', ' ', text)

    # remove tabs
    text = re.sub(r'[\t]+', ' ', text)

    # remove double quotes
    text = text.replace('"', '')

    # remove fancy quotes
    text = text.replace('“', '')
    text = text.replace('”', '')

    # collapse multiple spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

for col in df.columns:

    if df[col].dtype == "object":

        df[col] = df[col].apply(clean_text)

print("Text Cleaning Completed")
print()

# ==========================================
# CLEAN DATES
# ==========================================

print("Cleaning Dates...")

date_columns = [
    "Purchase Date",
    "Return Date",
    "Review Date"
]

for col in date_columns:

    if col in df.columns:

        df[col] = pd.to_datetime(
            df[col],
            errors="coerce",
            dayfirst=True
        )

        df[col] = df[col].dt.strftime("%Y-%m-%d")

print("Date Cleaning Completed")
print()

# ==========================================
# RENAME COLUMNS
# ==========================================

print("Renaming Columns...")

rename_dict = {

    "Product ID": "product_id",
    "Product Rating": "product_rating",
    "Review Comments": "review_comments",
    "Purchase Date": "purchase_date",
    "Return Date": "return_date",
    "Review Date": "review_date",
    "Category": "category"

}

df.rename(columns=rename_dict, inplace=True)

print("Column Rename Completed")
print()

print("Final Columns:")
print(df.columns.tolist())
print()

# ==========================================
# VERIFY NO NEWLINES EXIST
# ==========================================

print("Checking For Remaining Newlines...")

newline_found = False

for idx, row in df.iterrows():

    if "review_comments" in df.columns:

        if "\n" in str(row["review_comments"]):

            newline_found = True

            print("Found newline at row:", idx)

if not newline_found:

    print("SUCCESS: No newline characters found")

print()

# ==========================================
# EXPORT CSV
# ==========================================

output_file = "output/products_postgresql.csv"

df.to_csv(

    output_file,

    index=False,

    encoding="utf-8",

    quoting=csv.QUOTE_ALL

)

print("===================================")
print("CLEANING COMPLETED")
print("===================================")
print()

print("Output File:")
print(output_file)
print()

print(df.head())