import json
import math
from datetime import datetime
import requests


def get_currency():
    with open('currency/currency.json', 'r') as file:
        data = json.load(file)
    current_date = datetime.today()
    date_format = "%Y-%m-%d"
    date_object = datetime.strptime(data['Date'], date_format)
    if date_object < current_date:
        course_data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

        with open('currency/currency.json', 'w', encoding='utf-8') as file:
            json.dump({'Value': course_data['Valute']['CNY']['Value'], 'Date': current_date.strftime(date_format)}, file)
            return round(course_data['Valute']['CNY']['Value'], 2)
    return round(int(data['Value']), 2)