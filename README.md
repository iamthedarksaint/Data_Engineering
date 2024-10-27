
Welcome to my Data Engineering journey, where I am documenting my weekly progress as I learn and build hands-on projects. This ongoing project covers various aspects of data engineering, from data extraction and automation to workflow orchestration and database integration. Each week focuses on a different aspect, building upon the skills and concepts learned previously.

Project Overview

This project aims to chronicle my learning journey in data engineering through weekly tasks. I started with foundational skills and gradually tackled more complex topics, such as API integration, workflow automation, data storage, and pipeline development. The project is structured by week, with each week introducing new tools and techniques to help build end-to-end data engineering workflows.

Weeks Overview

Week 1: Getting Started
Topic: Basic Data Exploration
Summary:
Explored the fundamentals of data analysis using Pandas and Jupyter Notebook.
Analyzed the Titanic dataset to get familiar with data cleaning and basic transformations.
Pushed the project to GitHub to manage version control.

Week 2: Command Line Tools and OOP
Topic: Python Scripting and Code Structuring
Summary:
Learned about argparse, click, and logging for command-line interface (CLI) development.
Practiced Object-Oriented Programming (OOP) principles to better organize the code.
Continued pushing projects to GitHub for version control.

Week 3: API Integration and Workflow Orchestration
Topic: Automating Data Workflows
Summary:
Integrated data from SofaScore API, converting it to JSON and saving it in Parquet and Excel formats.
Automated data fetching using Prefect for workflow orchestration.
Managed sensitive information using python-decouple.
Collaborated on GitHub, following proper branching strategies.

Week 4: Connecting Data to PostgreSQL
Topic: Data Storage and Database Integration
Summary:
Set up PostgreSQL for data storage.
Automated data flow from API to PostgreSQL.
Enhanced data pipeline skills by integrating multiple components.

Week 5: FastAPI and API Development
Topic: Building a RESTful API
Summary:
Created FastAPI endpoints for CRUD operations with PostgreSQL.
Integrated SQLAlchemy for object-relational mapping.
Tested endpoints with Postman and implemented data validation and error handling.

Week 6: Cloud Hosting and Data Warehousing
Topic: Making the Project Accessible
Summary:
Migrated from local PostgreSQL to Supabase as a cloud-based data warehouse.
Deployed the FastAPI to Vercel for public access and testing.
Gained experience in managing cloud-hosted services.
Tech Stack

Programming Language: Python
Tools & Libraries: Jupyter Notebook, Pandas, Prefect, requests, argparse, FastAPI, SQLAlchemy, python-decouple
Databases: PostgreSQL, Supabase
Version Control: Git & GitHub
Cloud Services: Vercel (for FastAPI deployment), Supabase (for data warehousing)
How to Run the Project

Clone the Repository:
git clone https://github.com/iamthedarksaint/DataEngineeringJourney.git

Install Dependencies:
pip install -r requirements.txt

Configure Environment Variables:
Add necessary configuration for API keys, database credentials, and other sensitive information using a .env file.

Run Individual Week's Project:
Navigate to the respective week's folder (e.g., week1, week2) and follow the README instructions for that week.
Project Structure

The repository is structured by week, with each week containing:

Python scripts for the weekly tasks.
README files explaining what was learned and how to execute the code.
Requirements.txt for dependencies.
python
├── week1/
│   ├── titanic.ipynb
│   ├── README.md
│   └── requirements.txt
├── week2/
│   ├── script.py
│   ├── README.md
│   └── requirements.txt
├── week3/
│   ├── workflow.py
│   ├── README.md
│   └── requirements.txt
...
Ongoing Work and Future Plans

The project is a continuous effort, and I will keep updating the repository as I progress through the weeks. Upcoming topics may include:

Data Streaming
ETL (Extract, Transform, Load) Processes
Cloud Data Storage Solutions
Data Lake and Data Warehouse Architectures
Lessons Learned

Throughout this journey, I've gained a deeper understanding of:

Data pipeline automation using various tools.
Best practices for secure coding and handling sensitive data.
Collaborative coding workflows using GitHub.
Contact

Feel free to connect with me on https://linkedin.com/in/hassanazeezabiodun or follow my progress on https://x.com/iamthedarksaint.

