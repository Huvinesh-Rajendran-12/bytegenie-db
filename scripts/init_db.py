from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
# Exporting Data to Database
load_dotenv()

df_company = pd.read_csv("../data/updated_company_info.csv")
df_event = pd.read_csv("../data/updated_event_info.csv")
df_people = pd.read_csv("../data/updated_people_info.csv")

# Get the database credentials from environment variables
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

db_url = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
# Create a database engine
engine = create_engine(db_url)

df_company.to_sql('company', engine, if_exists='replace', index=False)
df_event.to_sql('event', engine, if_exists='replace', index=False)
df_people.to_sql('people', engine, if_exists='replace', index=False)
