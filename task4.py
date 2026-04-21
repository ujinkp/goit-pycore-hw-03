from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Valentyn", "birthday": "2026.04.25"}
]
def get_upcoming_birthdays(users):
    current_day = datetime.today().date()
    week_birthdays = []

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=current_day.year)
        if user_birthday < current_day:
            user_birthday = user_birthday.replace(year=current_day.year + 1)
        
        days_difference = (user_birthday - current_day).days
        if 0 <= days_difference <= 7:
            day_of_week = user_birthday.weekday()
            if day_of_week == 5:
                user_birthday += timedelta(days=2)
            elif day_of_week == 6:
                user_birthday += timedelta(days=1)
        
            week_birthdays.append({
                "name": user["name"],
                "congratulation_date": user_birthday.strftime("%Y.%m.%d")
            })

    return week_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)