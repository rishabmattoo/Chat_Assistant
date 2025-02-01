import sqlite3
import re
from datetime import datetime

class QueryProcessor:
    def __init__(self):
        self.conn = sqlite3.connect('database/company.db', check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def process_query(self, user_input):
        try:
            user_input = user_input.lower().strip()
            
            # Pattern 1: Employees in department
            if 'show me all employees in the' in user_input:
                department = self._extract_pattern(r'in the (.*?) department', user_input)
                return self._get_employees_by_department(department)
            
            # Pattern 2: Department manager
            elif 'who is the manager of the' in user_input:
                department = self._extract_pattern(r'of the (.*?) department', user_input)
                return self._get_department_manager(department)
            
            # Pattern 3: Employees hired after date
            elif 'list all employees hired after' in user_input:
                date_str = self._extract_pattern(r'after (.*?)$', user_input)
                return self._get_employees_hired_after(date_str)
            
            # Pattern 4: Total salary by department
            elif 'what is the total salary expense for the' in user_input:
                department = self._extract_pattern(r'for the (.*?) department', user_input)
                return self._get_total_salary(department)
            
            else:
                return {'error': 'Unsupported query format'}

        except Exception as e:
            return {'error': str(e)}

    def _extract_pattern(self, pattern, text):
        match = re.search(pattern, text)
        if not match:
            raise ValueError('Could not extract information from query')
        return match.group(1).title()

    def _get_employees_by_department(self, department):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Employees WHERE Department = ?', (department,))
        results = cursor.fetchall()
        return [dict(row) for row in results] if results else {'message': 'No employees found'}

    def _get_department_manager(self, department):
        cursor = self.conn.cursor()
        cursor.execute('SELECT Manager FROM Departments WHERE Name = ?', (department,))
        result = cursor.fetchone()
        return {'manager': result['Manager']} if result else {'error': 'Department not found'}

    def _get_employees_hired_after(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM Employees WHERE Hire_Date > ?', (date_str,))
            results = cursor.fetchall()
            return [dict(row) for row in results] if results else {'message': 'No employees found'}
        except ValueError:
            return {'error': 'Invalid date format. Use YYYY-MM-DD'}

    def _get_total_salary(self, department):
        cursor = self.conn.cursor()
        cursor.execute('SELECT SUM(Salary) AS total FROM Employees WHERE Department = ?', (department,))
        result = cursor.fetchone()
        return {'total_salary': result['total']} if result['total'] else {'error': 'Department not found'}
