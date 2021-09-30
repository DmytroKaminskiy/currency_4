import requests
from bs4 import BeautifulSoup

from writers import TXTWriter, CSVWriter, JSONWriter, DBWriter


ROOT = 'https://www.work.ua'


full_url = ROOT + '/ru/jobs/'

page = 0

writers_list = [
    TXTWriter(),
    CSVWriter(),
    JSONWriter(),
    DBWriter(),
]

while True:
    page += 1
    print(f'Page: {page}')

    params = {
        'page': page,
    }

    response = requests.get(full_url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_list_container = soup.find("div", {"id": "pjax-job-list"})

    # no jobs left
    if job_list_container is None:
        break

    jobs = job_list_container.find_all('div', {'class': 'card card-hover card-visited wordwrap job-link js-hot-block'})

    for job in jobs:
        href = job.find('a')['href']
        id_ = ''.join(char for char in href if char.isdigit())
        title = job.find('a').text
        job_info = {
            'href': href,
            'title': title,
            'id': id_,
        }

        for writer in writers_list:
            writer.write(job_info)

for writer in writers_list:
    writer.destruct()
