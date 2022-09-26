# парсер для hh.ru
from random import randint
import time
import requests as req
from bs4 import BeautifulSoup
import json
import tqdm

data = {
    'data': []
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

url = f"https://murmansk.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50"
# url = f"https://murmansk.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=unity&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50"

resp = req.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "lxml")
# извлекаем количество страниц в результате поиска
count_pages = int(soup.find_all(attrs={"class": "pager-item-not-in-short-range"})[-1].find(attrs={"rel": "nofollow"}).text)
vacancy_amount = 0

for page in range(1, count_pages):
    # for page in range(1, 2):
    time.sleep(randint(2, 5))
    url = f"https://murmansk.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50"
    resp = req.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "lxml")
    # Получаем список вакансий с адресами
    tags = soup.find_all(attrs={"class": "serp-item__title"})
    # Перебираем вакансии
    # for i in tags:
    for i in tqdm.tqdm(tags):
        time.sleep(randint(2, 5))
        # получаем страницу для каждой вакансии
        url_vacancy = i.attrs["href"]
        # print(url_vacancy)
        title = i.text  # вакансия
        # Запрос к странице конкретной вакансии
        resp_vacancy = req.get(url_vacancy, headers=headers)
        soup_object = BeautifulSoup(resp_vacancy.text, 'html.parser')
        # извлекаем зарплату
        try:
            salary = soup_object.find(attrs={"data-qa": "vacancy-salary"}).find(
                attrs={"class": "bloko-header-section-2"}).text
        except:
            salary = "NONE"
        # Извлекаем опыт работы
        try:
            work_experience = soup_object.find(attrs={"class": "vacancy-description-list-item"}).text
        except:
            work_experience = "NONE"
        # Извлекаем регион
        try:
            region = soup_object.find(attrs={"data-qa": "vacancy-view-location"}).text
        except:
            region = "NONE"

        vacancy_amount += 1
        print(f"№ {vacancy_amount}: ", title, work_experience, salary, region, sep=' | ')

        data['data'].append({'title': i.text, 'work_experience': work_experience, 'salary': salary, 'region': region})
        with open("data.json", "w") as f:
            json.dump(data, f, ensure_ascii=False)
print(f"Всего вакансий - {vacancy_amount}")
