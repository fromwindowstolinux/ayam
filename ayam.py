import datetime
import pandas
import random
from faker import Faker

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 31)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days


states = ["Perlis", "Kedah", "Pulau Pinang", "Perak", "Selangor", "Johor", "Negeri Sembilan", "Melaka", "Pahang", "Terengganu", "Kelantan", "Sabah", "Sarawak", "Kuala Lumpur", "Putrajaya", "Labuan"]
fastfood = ["KFC", "Mc Donalds", "Texas Chicken", "A&W", "Marrybrown"]

fake = Faker()
Faker.seed(0)

with open('ayam.csv', 'w') as f:
    f.write('Date,state,fastfood,Total_Sales\n')
    for _ in range(10):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        f.write(random_date.strftime('%F'))
        f.write(',')
        f.write(random.choice(states))
        f.write(',')
        f.write(random.choice(fastfood))
        f.write(',')
        f.write(str(fake.pyint()))
        f.write('\n')