# SQLite Chat Assistant

A Flask-based chat interface that converts natural language queries into SQL for an employee/department database.

## Features
- Regex-based query processing
- 4 supported query types
- Web interface with tabular results
- Error handling for invalid inputs

## Quick Start

1. Clone repo and install dependencies:
   ```bash
   git clone https://github.com/yourusername/chat-assistant.git
   cd chat-assistant
   pip install -r requirements.txt
2. Initialize database:
   python database/create_db.py
   
4. Run app:
   python app.py

Visit http://localhost:5000

## Example Queries
"Show employees in Sales"

"Engineering department manager"

"Employees hired after 2021-01-01"

"Marketing total salary"

## Limitations
Fixed query patterns

Requires exact date format (YYYY-MM-DD)

Basic error messages

## Suggested Improvements
Add more query types

Improve date parsing

Enhanced UI/UX

SQL injection protection

