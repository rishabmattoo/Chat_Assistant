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

## 🚀 Deployment on Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Click the "Deploy to Render" button above
2. Connect your GitHub account
3. Select repository
4. Add these environment variables:
   - **Key:** `PORT`  
     **Value:** `5000`
5. Under "Advanced":
   ```text
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
My Deployment link: https://chat-assistant-2-hxw7.onrender.com/
