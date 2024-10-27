Project Overview

Building on the API work from Week 5, Week 6 was all about moving from a local setup to the cloud. I transitioned the data warehouse to Supabase, making it accessible globally, and hosted the API on Vercel for public testing.

Key Accomplishments:
Cloud Data Warehouse Migration: Migrated from local PostgreSQL to Supabase, enabling cloud-based storage and data accessibility.
Deployment on Vercel: Hosted the FastAPI project on Vercel, making the API accessible for public use and testing.
Database Connectivity Optimization: Ensured smooth integration between FastAPI and Supabase, focusing on performance improvements.
Continued Testing & Refinement: Collected feedback from testers, fine-tuning data validation, error handling, and overall performance.
Technologies Used:
FastAPI: Continued use for the API layer.
Supabase: As the cloud data warehouse solution.
Vercel: For deploying and hosting the API.
Postman: For ongoing testing and validation.
How to Run Week 6 Project:
Clone the Repository:
bash
Copy code
git clone https://github.com/iamthedarksaint/week6.git

Install Dependencies:

pip install -r requirements.txt
Set Up Environment Variables:
Configure Supabase URL and API keys in a .env file.

Run the FastAPI Application Locally:

uvicorn main:app --reload
Live API Testing:
The API is also accessible at sofascoreapi.vercel.app on Vercel.
