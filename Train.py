import datetime
from builtins import print
import calendar

welcome_massage = "Hello World, lets try to learn Python"
current_year = datetime.date.today().year
my_birth_year = 1996
my_birth_day = 22
my_birth_month = 1
my_birth_date = datetime.date(my_birth_year, my_birth_month, my_birth_day)
my_age = current_year - my_birth_year
today_day = datetime.date.today()
my_accurate_age = (today_day - my_birth_date).days
today_weekday = calendar.day_name[datetime.date.today().weekday()]
current_time = datetime.datetime.now().time()

my_current_vibe = "I can do this. I'm gonna learn Python QA Automation"

print(welcome_massage, "Чтож, го потренируемся")
print("Возраст",  my_age)
print("Мой точный возраст в днях", my_accurate_age)
print("День недели", today_weekday)
print("Точное время", current_time.strftime("%H:%M:%S"))
print("Сегодняшний вайб", my_current_vibe)