from datetime import datetime

def get_days_from_today(date):
    try:    
        delta = datetime.today().date() - datetime.strptime(date, "%Y-%m-%d").date()
        return delta.days
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."


print(get_days_from_today("2020-10-09"))