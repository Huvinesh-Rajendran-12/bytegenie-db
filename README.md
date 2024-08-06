# ByteGenie Database

This repository contains the database schema and related information for my ByteGenie FullStack Developer Test application.

## Technology Stack

- PostgreSQL 13+
- SQLAlchemy (for ORM and migrations)
- Python 3.9+

## Setup and Installation

1. **Install PostgreSQL:**
   Follow the instructions for your operating system from the [official PostgreSQL website](https://www.postgresql.org/download/).

2. **Create a new database:**
   Open a terminal and run the following commands:

   ```sql
   # Connect to PostgreSQL as the postgres user
   sudo -u postgres psql

   # Create the database
   CREATE DATABASE bytegenie;

   # Create a new user (replace 'your_username' and 'your_password' with your preferred credentials)
   CREATE USER your_username WITH PASSWORD 'your_password';

   # Grant privileges to the new user on the bytegenie database
   GRANT ALL PRIVILEGES ON DATABASE bytegenie TO your_username;

   # Exit psql
   \q
   ```

3. **Set up the Python environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following:

   ```
   DB_USERNAME=bytegenie_user
   DB_PASSWORD=bytegenie_pass
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=bytegenie_db
   ```

5. **Initialize the database:**
   ```bash
   cd scripts
   python init_db.py
   ```

## Database Schema

The database consists of the following main tables:

### `company`

- company_logo_url (text)
- company_logo_text (text)
- company_name (text)
- relation_to_event (text)
- event_url (text)
- company_revenue (text)
- n_employees (text)
- company_phone (text)
- company_founding_year (text)
- company_address (text)
- company_industry (text)
- company_overview (text)
- homepage_url (text)
- linkedin_company_url (text)
- homepage_base_url (text)
- company_logo_url_on_event_page (text)
- company_logo_match_flag (text)

### `event`

- event_logo_url (text)
- event_name (text)
- event_start_date (text)
- event_end_date (text)
- event_venue (text)
- event_country (text)
- event_description (text)
- event_url (text)
- event_industry (text)

### `people`

- first_name (text)
- middle_name (text)
- last_name (text)
- job_title (text)
- person_city (text)
- person_state (text)
- person_country (text)
- email_pattern (text)
- homepage_base_url (text)
- duration_in_current_job (text)
- duration_in_current_company (text)
- email_address (text)

**Note:** All columns are of type 'text' according to the provided schema.

### Key Relationships

- The `company` and `event` tables are related through the `event_url` field.
- The `company` and `people` tables are related through the `homepage_base_url` field.

## Challenges I Faced

During the database design and implementation, I encountered the following challenges:

1. Efficiently linking events, companies, and people data
2. Handling inconsistencies in the original CSV data
3. Maintaining the accuracy of the data even through augmentations
4. Deriving and standardizing additional columns (e.g., event_industry, email_address)
5. Ensuring data integrity across related tables

## Future Improvements

If I had more time, I would improve the database design in the following ways:

1. Implement partitioning for large tables to improve query performance
2. Add more advanced indexing strategies based on common query patterns
3. Add full-text search capabilities for more efficient text-based queries
4. Develop a comprehensive data validation and cleaning pipeline
5. Implement a caching layer for frequently accessed data
