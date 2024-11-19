Project Overview

In Week3, I delved into workflow orchestration using Prefect, explored real-time data processing, and enhanced my skills in API integration. This week was focused on automating data workflows, securely managing environments, and collaborating effectively using Git.

Key Accomplishments:

API Integration:
Fetched live sports data from SofaScore using the requests library.
Transformed the fetched data into a Pandas DataFrame after converting it from JSON format.
Saved the processed data in both Parquet and Excel formats for efficient storage and analysis.

Workflow Automation with Prefect:
Automated the fetching and processing of live data using Prefect as the orchestration tool.
Scheduled periodic data updates, ensuring the data remained current and refreshed at set intervals.

Environment & API Management:
Implemented python-decouple to securely handle the API key and other sensitive information via an .env file.
Followed best practices for keeping sensitive information outside the codebase.

Collaboration & Version Control:
Pushed the project to GitHub, collaborating with a friend using proper branching strategies for development, testing, and production environments.
Practiced version control techniques for better team collaboration.

Expanded Tech Stack:
Continued to build on knowledge of argparse, logging, CLI development, and Git, enhancing the efficiency of workflows and code organization.

Technologies Used:
Libraries & Tools: Prefect, requests, Pandas, python-decouple
Data Formats: JSON, Parquet, Excel

Version Control: Git & GitHub

How to Run the Week 3 Project:

Clone the Repository:
git clone https://github.com/iamthedarksaint/week3.git

Install Dependencies:
pip install -r requirements.txt

Set Up the .env File:
Create a .env file in the project directory and add your API key:
makefile
API_KEY=your_api_key_here

Run the Prefect Flow:
prefect run -n fetch_live_data
Check the Output Files:
The data will be stored in the output directory as both Parquet and Excel files.
