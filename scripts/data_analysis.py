import pandas as pd
import re
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

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
print(rows_with_special_chars["company_name"])

rows_with_special_chars = rows_with_special_characters(df_event, 'event_name', special_chars)
print("Rows with special characters in 'event_name':")
print(rows_with_special_chars["event_name"])

print(df_event.info())

print(df_people.tail(5))
print(df_people.info())

# Merging DataFrames
df_company_event = pd.merge(df_company, df_event, on="event_url", how="inner")
print(df_company_event.info())
print(df_company_event.head(5))

df_people_company = pd.merge(df_people, df_company, on="homepage_base_url", how="inner")
print(df_people_company.info())
print(df_people_company.head())

# Exporting Data as CSV files
df_company_event.to_csv("./data/company_event.csv", index=False, encoding="utf-8-sig")
df_people_company.to_csv("./data/people_company.csv", index=False, encoding="utf-8-sig")

# Reading LLM updated Data
df_processed_company_event = pd.read_csv("./data/company_event_with_industry.csv")
print(df_processed_company_event.info())
print(df_processed_company_event.head())

df_processed_company_people = pd.read_csv("./data/updated_people_company.csv")
print(df_processed_company_people.info())
print(df_processed_company_people.head())

# Exporting Data to Database
load_dotenv()

# Get the database credentials from environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

db_url = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
# Create a database engine
engine = create_engine(db_url)

print(db_name)

df_company.to_sql('company', engine, if_exists='replace', index=False)
df_event.to_sql('event', engine, if_exists='replace', index=False)
df_people.to_sql('people', engine, if_exists='replace', index=False)
