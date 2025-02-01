SQLite Chat Assistant

A Python-based chat assistant that interacts with an SQLite database to answer natural language queries about employees and departments.

How It Works

Components

Natural Language Processing

Uses regex patterns to convert natural language queries into SQL commands.

Supported query patterns include:

Department employee listings

Department manager identification

Employee hire date filtering

Department salary totals

Database Structure

SQLite database with two tables:

Employees (ID, Name, Department, Salary, Hire_Date)

Departments (ID, Name, Manager)

Web Interface

Built with Flask, featuring:

Real-time chat-like interface

Tabular results display

Error message handling

Query Processing

Converts user input to SQL queries

Executes against the database

Returns formatted JSON responses

Local Installation

Requirements

Python 3.7+

Flask

SQLite3

Setup Steps

Install Dependencies

pip install -r requirements.txt

Initialize Database

python database/create_db.py

Start Application

python app.py

Access Interface
Open http://localhost:5000 in your browser.

Testing

Try these sample queries:

"Show me all employees in the Sales department"

"Who is the manager of the Engineering department?"

"List all employees hired after 2021-01-01"

"What is the total salary expense for the Marketing department?"

Limitations

Current Constraints

Query Patterns: Limited to four predefined question formats

Date Handling: Requires exact YYYY-MM-DD format

Error Messages: Basic error reporting without detailed explanations

UI Features

No chat history persistence

Basic text formatting

No user authentication

Suggested Improvements

Enhanced NLP

Integrate lightweight NLP library (e.g., spaCy) for better query understanding

Query Expansion

Add support for:

Employee search by name

Salary range queries

Department performance metrics

Security

Add SQL injection protection

Implement rate limiting

UI Enhancements

Chat history storage

Export results to CSV/PDF

Interactive query builder

Database

Add data validation constraints

Implement proper indexing

Add audit logging
