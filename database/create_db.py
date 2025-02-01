import sqlite3

def initialize_database():
    conn = sqlite3.connect('database/company.db')  # Connect to SQLite database
    c = conn.cursor()
    
    # Create Employees Table
    c.execute('''CREATE TABLE IF NOT EXISTS Employees (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Department TEXT NOT NULL,
                Salary REAL,
                Hire_Date DATE)''')
    
    # Create Departments Table
    c.execute('''CREATE TABLE IF NOT EXISTS Departments (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Manager TEXT NOT NULL)''')
    
    # Insert Sample Data Only If Tables Are Empty
    c.execute("SELECT COUNT(*) FROM Employees")
    if c.fetchone()[0] == 0:
        employees = [
            (1, 'Alice', 'Sales', 50000, '2021-01-15'),
            (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
            (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
        ]
        c.executemany('INSERT INTO Employees VALUES (?,?,?,?,?)', employees)
    
    c.execute("SELECT COUNT(*) FROM Departments")
    if c.fetchone()[0] == 0:
        departments = [
            (1, 'Sales', 'Alice'),
            (2, 'Engineering', 'Bob'),
            (3, 'Marketing', 'Charlie')
        ]
        c.executemany('INSERT INTO Departments VALUES (?,?,?)', departments)
    
    conn.commit()  # Save changes
    conn.close()   # Close connection

if __name__ == '__main__':
    initialize_database()  # Run function to initialize the database
