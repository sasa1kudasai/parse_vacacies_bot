import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
headers = {'User-Agent': user_agent}

def parse_vacancies(query):
    vacancies = []
    for i in range(1, 10):
        url = f"https://www.work.ua/jobs-remote-it-{query}/?advs=1&anyword=1&notitle=1&nosynonym=1&page={i}"
        response = requests.get(url, headers=headers)
        print(i, response, url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            elements_with_class = soup.find_all(class_="card card-hover card-visited wordwrap job-link")
            # Здесь парсим HTML страницу и извлекаем информацию о вакансиях
            # Пример: для каждой вакансии извлекаем название и ссылку
            for vacancy_element in elements_with_class:
                a_tag = vacancy_element.find('a')

                title = a_tag.text.strip()
                link = 'https://www.work.ua' + a_tag['href']
                vacancies.append({'title': title, 'link': link})
    return vacancies

