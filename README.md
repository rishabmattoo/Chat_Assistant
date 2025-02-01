# SQLite Chat Assistant

A Python-based chat assistant that interacts with an SQLite database to answer natural language queries about employees and departments.

## How It Works

### Components
1. **Natural Language Processing**:  
   Uses regex patterns to convert natural language queries into SQL commands.  
   Supported query patterns include:
   - Department employee listings
   - Department manager identification
   - Employee hire date filtering
   - Department salary totals

2. **Database Structure**:  
   SQLite database with 2 tables:
   ```sql
   Employees (ID, Name, Department, Salary, Hire_Date)
   Departments (ID, Name, Manager)
3. **Web Interface**:
Built with Flask, featuring:

Real-time chat-like interface

Tabular results display

Error message handling

4. **Query Processing**:

Converts user input to SQL queries

Executes against database

Returns formatted JSON responses

5. **Local Installation**
Requirements
Python 3.7+

Flask

SQLite3

Setup Steps

6. **Install Dependencies**
pip install -r requirements.txt
Initialize Database


python database/create_db.py
7.**Start Application**


python app.py
8. **Access Interface**
Open http://localhost:5000 in your browser

(. **Testing**
Try these sample queries:

"Show me all employees in the Sales department"

"Who is the manager of the Engineering department?"

"List all employees hired after 2021-01-01"

"What is the total salary expense for the Marketing department?"

9. **Limitations**
Current Constraints
Query Patterns
Limited to 4 predefined question formats

10. **Date Handling**
Requires exact YYYY-MM-DD format

11. **Error Messages**
Basic error reporting without detailed explanations

12. **UI Features**

No chat history persistence

Basic text formatting

No user authentication

13. **Suggested Improvements**
Enhanced NLP
Integrate lightweight NLP library (e.g., spaCy) for better query understanding

***Query Expansion***
Add support for:

Employee search by name

Salary range queries

Department performance metrics

***Security***

Add SQL injection protection

Implement rate limiting

***UI Enhancements***

Chat history storage

Export results to CSV/PDF

Interactive query builder

***Database***

Add data validation constraints

Implement proper indexing

Add audit logging

14. **Project Structure**

chat-assistant/
├── database/
│   ├── company.db        # Database file
│   └── create_db.py      # Initialization script
├── templates/
│   └── index.html        # Web interface
├── app.py                # Flask application
├── queries.py            # Query processor
└── requirements.txt      # Dependencies   
