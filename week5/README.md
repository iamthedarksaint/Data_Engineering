Week 5: FastAPI, PostgreSQL, and API Testing

Project Overview
In Week 5, the focus was on building a solid API layer using FastAPI that interacts with a PostgreSQL database. The aim was to implement basic CRUD operations, ensure data integrity, and test the API rigorously.

Key Accomplishments:
FastAPI Endpoints: Developed endpoints for CRUD operations (Create, Read, Update, Delete), allowing interaction with the PostgreSQL database.
Database Integration: Utilized SQLAlchemy for Object-Relational Mapping (ORM) to simplify database operations and maintain data consistency.
API Testing: Conducted thorough testing of each endpoint using Postman to ensure proper functionality.
Data Validation & Error Handling: Implemented data validation techniques and custom error messages to enhance API robustness.
Response Models: Set up response models for consistent API responses and better documentation.
Technologies Used:
FastAPI: For developing the API.
PostgreSQL: As the database for data storage.
SQLAlchemy: For ORM and database connectivity.
Postman: For testing API endpoints.

How to Run Week 5 Project:

Clone the Repository:
git clone https://github.com/your-username/week5-project.git

Install Dependencies:
pip install -r requirements.txt
Set Up PostgreSQL Database:
Configure the PostgreSQL database connection in the .env file.

Run the FastAPI Application:
uvicorn main:app --reload
Access the API Documentation:
Navigate to http://127.0.0.1:8000/docs for Swagger UI.

