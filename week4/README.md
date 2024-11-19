Project Overview

In Week 4, I focused on integrating API-fetched data into a PostgreSQL database, taking my data pipeline skills to the next level. This week was about building on the previous work of fetching data from APIs and now connecting it to a structured database for better data management and accessibility.

Key Accomplishments:

Set Up PostgreSQL:
Installed and configured PostgreSQL for use as a storage solution for the fetched data.

Data Integration:
Connected the API data to the PostgreSQL database, allowing for seamless data transfer and storage.
Automated the data ingestion process, making the data pipeline more efficient by regularly updating the database with fresh data.

Enhanced Data Pipeline Skills:
Continued to develop automation skills by integrating multiple components of the data engineering process, from data fetching to database management.

Technologies Used:
Libraries & Tools: PostgreSQL, requests, Pandas
Database: PostgreSQL
Version Control: Git & GitHub

How to Run the Week 4 Project:

Clone the Repository:
git clone https://github.com/iamthedarksaint/week4.git

Install Dependencies:
pip install -r requirements.txt

Configure the Database:
Set up PostgreSQL and create the necessary database.
Update the database connection settings in the configuration file.

Set Up the .env File:
Add your database credentials and API key to a .env file:
API_KEY=your_api_key_here
DB_USER=your_db_username
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_NAME=your_db_name

Run the Data Pipeline Script:
python run_pipeline.py
Verify the Data in PostgreSQL:
Check the database to ensure the fetched data is properly stored and updated.
