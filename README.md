# ByteGenie Database

This repository contains the database schema and related information for my ByteGenie FullStack Developer Test application.

## Technology Stack

- PostgreSQL 13+
- SQLAlchemy (for ORM and migrations)
- Python 3.9+

## Setup and Installation

1. Install PostgreSQL:
   Follow the instructions for your operating system from the [official PostgreSQL website](https://www.postgresql.org/download/).

2. Create a new database:
   Open a terminal and run the following commands:

   ```
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

3. Set up the Python environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:

   ```
   DB_USERNAME=bytegenie_user
   DB_PASSWORD=bytegenie_pass
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=bytegenie_db
   ```

5. Initialize the database
   ```
   cd scripts
   python init_db.py
   ```

## Database Schema

The database consists of the following main tables:

1. `events`

   - event_url (Primary Key)
   - event_name
   - event_description
   - event_start_date
   - event_end_date
   - event_venue
   - event_country
   - event_industry (derived)

2. `companies`

   - homepage_base_url (Primary Key)
   - company_name
   - company_industry
   - company_revenue
   - number_of_employees

3. `people`

   - id (Primary Key)
   - first_name
   - last_name
   - job_title
   - email_address (derived)
   - company_homepage_base_url (Foreign Key to companies)

## Challenges I Faced

During the database design and implementation, I encountered the following challenges:

1. Efficiently linking events, companies, and people data
2. Handling inconsistencies in the original CSV data
3. Maintaning the accuracy of the data even through augmentations
4. Deriving and standardizing additional columns (e.g., event_industry, email_address)
5. Ensuring data integrity across related tables

## Future Improvements

If I had more time, I would improve the database design in the following ways:

1. Implement partitioning for large tables to improve query performance
2. Add more advanced indexing strategies based on common query patterns
3. Add full-text search capabilities for more efficient text-based queries
4. Develop a comprehensive data validation and cleaning pipeline
5. Implement a caching layer for frequently accessed data
6. Add support for real-time data updates and change data capture (CDC)
