def calculator(age_year):
    days_in_year = 365.25
    hours_in_days = 24
    minutes_in_hour = 60

    total_days = age_year*days_in_year
    total_hours = total_days*hours_in_days
    total_minutes = total_hours*minutes_in_hour
    return round(total_days),round(total_hours),round(total_minutes)
while True:
    try:
        age = float(input('enter your age in years:'))
        days,hours,minutes = calculator(age)
        print('\n your approx age ')
        print(f' - {days} days old')
        print(f'- {hours} hours old')
        print(f'- {minutes} minutes old')

        again = input('whould you like to try again ? (y/n)').strip().lower()
        if again !='y':
            print('good bye')
            break
    except:
        print('please enter a valid number for age')
        
