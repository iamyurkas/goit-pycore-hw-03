import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or max <= min or quantity > (max - min):
        return []
    return sorted(random.sample(range(min, max), quantity))

print(get_numbers_ticket(1, 1000, 3))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(10, 11, 12))