import random

def get_numbers_ticket(min, max, quantity):
    if min < max and min >= 1 and max <=1000 and quantity <= (max - min + 1):
        lottery_numbers = random.sample((range(min, max + 1)), quantity)
        return sorted(lottery_numbers)
    else:
        return []
    
try:
    min = int(input("Введіть мінімальне можливе число у наборі (не менше 1): "))
    max = int(input("Введіть максимальне можливе число у наборі (не більше 1000): "))
    quantity = int(input("Введіть кількість чисел, які потрібно вибрати: "))
    lottery_numbers = get_numbers_ticket(min, max, quantity)
    print("Ваші лотерейні числа:", lottery_numbers)
except Exception as e:
    print("Будь ласка, вводьте лише цілі числа.")