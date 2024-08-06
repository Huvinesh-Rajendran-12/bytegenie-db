import pandas as pd
import re

# Import Data
df_company = pd.read_csv("../data/updated_company_info.csv")
df_event = pd.read_csv("../data/updated_event_info.csv")
df_people = pd.read_csv("../data/updated_people_info.csv")


# Analyzing Data
print(df_company.info())

def rows_with_special_characters(df, column_name, special_chars):
    # Create a regex pattern from the list of special characters
    pattern = "[" + re.escape("".join(special_chars)) + "]"

    # Filter rows where the special characters exist in the specified column
    filtered_df = df[df[column_name].apply(lambda x: bool(re.search(pattern, x)) if isinstance(x, str) else False)]

    return filtered_df

# List of special characters to find
special_chars = ['#']

# Get rows with special characters in 'CompanyName'
rows_with_special_chars = rows_with_special_characters(df_company, 'company_name', special_chars)

print("Rows with special characters in 'company_name':")
print(len(rows_with_special_chars["company_name"]))

print(df_event.info())

rows_with_special_chars = rows_with_special_characters(df_event, 'event_name', special_chars)
print("Rows with special characters in 'event_name':")
print(len(rows_with_special_chars["event_name"]))


print(df_people.info())
