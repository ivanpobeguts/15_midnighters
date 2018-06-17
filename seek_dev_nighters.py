import requests


def load_attempts():
    base_url = 'https://devman.org/api/challenges/solution_attempts/'
    number_of_pages = requests.get(base_url).json()['number_of_pages']
    for page in range(1, number_of_pages + 1):
        users_info = requests.get(base_url + '?page=' + str(page))
        page_records_data = users_info.json()
        for record in page_records_data['records']:
            yield record


def get_midnighters():
    pass


if __name__ == '__main__':
    for record in load_attempts():
        print(record)
