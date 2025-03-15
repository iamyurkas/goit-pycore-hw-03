from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Get this year birtday
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)
        
        # Check if the birthdau in the past
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        # Check bitrhday week
        if 0 <= (birthday - today).days < 7:
            congratulation_date = adjust_for_weekend(birthday)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

def adjust_for_weekend(birthday):
    # Postpone if weekend
    if birthday.weekday() == 5:  # Saturday
        return birthday + timedelta(days = 2)
    elif birthday.weekday() == 6:  # Sunday
        return birthday + timedelta(days = 1)
    return birthday

users = [
    {"name": "John Doe",     "birthday": "1985.01.23"},
    {"name": "Jane Smith",   "birthday": "1990.01.27"},
    {"name": "John Doe 2",   "birthday": "1990.02.24"},
    {"name": "Jane Smith 2", "birthday": "1990.02.28"},
    {"name": "John Doe 3",   "birthday": "1990.03.15"},
    {"name": "Jane Smith 3", "birthday": "1990.03.17"},
    {"name": "John Doe 4",   "birthday": "1990.04.20"},
    {"name": "Jane Smith 4", "birthday": "1990.04.28"},
]

print(get_upcoming_birthdays(users))