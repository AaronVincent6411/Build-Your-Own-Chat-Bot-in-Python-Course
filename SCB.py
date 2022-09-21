import datetime

current_time = datetime.datetime.now()

city = input('Enter the city name\n')

hour = current_time.hour
minute = current_time.minute
second = current_time.second

if city == 'London':
    hour = hour + 5

elif city == 'Mumbai':
    hour = hour + 9
    minute = minute + 30

elif city == 'Tokyo':
    hour = hour + 13

else:
    print('City not added')
    exit(0)

print(city, str(hour)+":"+str(minute)+":"+str(second))