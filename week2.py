import datetime

# Task 1 - Calculating the price to park
def calculate_parking_price(day, arrival_hour, parking_hours, frequent_parking_number):
 
    if day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        return 'Invalid day entered.'
    
    if not (0 <= arrival_hour < 24):
        return 'Invalid arrival hour entered.'
    
    if not (0 < parking_hours <= 24):
        return 'Invalid parking hours entered.'
    
    if frequent_parking_number and not validate_frequent_parking_number(frequent_parking_number):
        return 'Invalid frequent parking number entered.'
    
    # Calculate discount
    discount = 0.5 if 16 <= arrival_hour <= 23 else 0.1
    
    # Calculate base price
    base_price = parking_hours * 2.5
    
    # Calculate price based on day
    if day.lower() == 'sunday':
        price = base_price - (base_price * discount)
    else:
        price = base_price
    
    return price

# Task 2 - Keeping a total of the payments
def calculate_daily_total_payments():
    daily_total = 0
    
    while True:
        amount_paid = float(input('Enter the amount paid (0 to exit): '))
        if amount_paid == 0:
            break
        
        daily_total += amount_paid
    
    return daily_total

# Task 3 - Making payments fairer
def calculate_parking_price_revised(day, arrival_hour, parking_hours, frequent_parking_number):
    if arrival_hour < 16:
        price_before_16 = calculate_parking_price(day, arrival_hour, 16 - arrival_hour, frequent_parking_number)
        price_after_16 = calculate_parking_price(day, 16, parking_hours - (16 - arrival_hour), frequent_parking_number)
        return price_before_16 + price_after_16
    else:
        return calculate_parking_price(day, arrival_hour, parking_hours, frequent_parking_number)


def validate_frequent_parking_number(number):
    if len(number) != 5:
        return False
    
    digits = number[:-1]
    check_digit = number[-1]
    
    if not digits.isdigit() or not check_digit.isdigit():
        return False
    
    total = sum(int(digit) * (10 - index) for index, digit in enumerate(digits))
    remainder = total % 11
    if remainder == 0:
        calculated_check_digit = 0
    else:
        calculated_check_digit = 11 - remainder
    
    return str(calculated_check_digit) == check_digit


day = input('Enter the day: ')
arrival_hour = int(input('Enter the arrival hour: '))
parking_hours = int(input('Enter the number of parking hours: '))
frequent_parking_number = input('Enter the frequent parking number (leave empty if not available): ')

price = calculate_parking_price(day, arrival_hour, parking_hours, frequent_parking_number)
print('Price to park:', price)


daily_total = calculate_daily_total_payments()
print('Daily total payments:', daily_total)


price_revised = calculate_parking_price_revised(day, arrival_hour, parking_hours, frequent_parking_number)
print('Revised price to park:', price_revised)