from datetime import datetime

specific_date = input("Input date: ")

def get_days_from_today(date):
    try:
        current_date = datetime.today().date()
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        difference = current_date - input_date
        return int(difference.days)
    
    except Exception as e:
        return "Введіть дату у форматі 'РРРР-ММ-ДД'"

result = get_days_from_today(specific_date)
print(result)