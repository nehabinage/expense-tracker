# Expense Tracker Django Project
- A simple Expense Tracker web application built using "Python" and "Django". To track your daily expenses, categorize them, and see total spending.

# Features
- Add new expenses with **name, amount, and category**  
- View all expenses in a clean table  
- See **total spending** at a glance  
- Categorize expenses: Food, Travel, Shopping, Other  
- Easy-to-use interface  
- Admin panel for managing expenses  

# Tech Stack
- Python 3.x  
- Django 5.x  
- HTML / CSS (for templates)  
- SQLite (default database)

# Project Structure
expense_tracker/
│
├── expense_tracker/ # Django project settings
├── tracker/ # Django app
│ ├── templates/ # HTML templates
│ │ ├── home.html
│ │ └── add_expense.html
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
├── manage.py

# Future Improvements
Edit / delete expenses
Filter expenses by category or date
Visual charts (pie/bar) for spending
User authentication for multiple users
