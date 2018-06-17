import requests
import datetime as dt
import pytz


def load_attempts():
    base_url = 'https://devman.org/api/challenges/solution_attempts/'
    number_of_pages = requests.get(base_url).json()['number_of_pages']
    for page_number in range(1, number_of_pages + 1):
        payload = {'page': str(page_number)}
        users_attempts = requests.get(base_url, params=payload)
        page_records_data = users_attempts.json()
        for record in page_records_data['records']:
            yield record


def get_midnighters(records):
    midnighters = set()
    start_time = dt.time(0, 0)
    end_time = dt.time(7, 0)
    for record in records:
        user_time = (dt.datetime.fromtimestamp(
            record['timestamp'],
            pytz.timezone(record['timezone'])
        ).time())
        if start_time < user_time < end_time:
            midnighters.add(record['username'])
    return midnighters


if __name__ == '__main__':
    midnighters = get_midnighters(load_attempts())
    for midnighter in midnighters:
        print(midnighter)
