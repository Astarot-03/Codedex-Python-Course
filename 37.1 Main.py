import datetime, bday_messages # file name is bday_messages.py, we import it as a module

today = datetime.date.today()
next_birthday = datetime.date(2027, 3, 22)

days_away = next_birthday - today

if next_birthday == today:
  print(bday_messages.random_message)
else:
  print(f'My next birthday is {days_away.days} days away!')


