from requests import get
from bs4 import BeautifulSoup
from database import CTF


def init(): #Инициализация перменных
  ad = 'https://ctftime.org/event/list/?year=2024&online=-1&format=0&restrictions=0&upcoming=true'
  ad2 = 'https://ctftime.org'
  r = get(ad,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'})
  soup = BeautifulSoup(r.text, 'lxml')
  ctfs_html = soup.select('tr:not(:first-of-type)')
  return ad, ad2, ctfs_html


def parse_links_from_page(url):
    response = get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        links_list = [link.get('href') for link in links if link.get('href') is not None]
        return links_list[24]
    else:
        print(f"Ошибка при получении страницы: {response.status_code}")
        return []

def place_insert(place): #Функция для подстановки места в словарь стф
  if place != '' and place[len(place)-1] != '\n' and place[0] != '\n':
    return place
  elif place != '' and place[0] == '\n' and place[len(place)-1] == '\n' and place[len(place)-2] == '\n' and place[1] == '\n':
    return place[6:len(place)-2]
  elif place != '' and place[0] == '\n' and place[len(place)-1] == '\n':
    return place[1:len(place)-1]
  elif place == '':
    return place


def ctf_text(ctf, first_text=''): #Отправка текста с стфкой
  if ctf["place"] != '' and ctf["place"] != 'On-line':
    return f'{first_text}Имя: {ctf["name"]}\nТип: {ctf["type"]}\nНачало: {ctf["begin_date"]} в {ctf["begin_time"]}\nКонец: {ctf["end_date"]} в {ctf["end_time"]}\nБудет проходить в {ctf["place"]}\nСсылка на страничку на ctf time: {ctf["link"]}'
  elif ctf['place'] == '':
    return f'{first_text}Имя: {ctf["name"]}\nТип: {ctf["type"]}\nНачало: {ctf["begin_date"]} в {ctf["begin_time"]}\nКонец: {ctf["end_date"]} в {ctf["end_time"]}\nМестоположение данной стф пока никому не известно...\nСсылка на страничку на ctf time: {ctf["link"]}'
  elif ctf['place'] == 'On-line':
    return f'{first_text}Имя: {ctf["name"]}\nТип: {ctf["type"]}\nНачало: {ctf["begin_date"]} в {ctf["begin_time"]}\nКонец: {ctf["end_date"]} в {ctf["end_time"]}\nБудет проходить в онлайн режиме\nСсылка на страничку на ctf time: {ctf["link"]}'


def all_ctf(session): #Функция для получения всех стфок
    ad, ad2, ctfs_html = init()
    ctfs = []
    
    for i in range(len(ctfs_html)):
      ctf_el = ctfs_html[i]
      ctf_html = BeautifulSoup(str(ctf_el), 'lxml').findAll('td')
      ctf = {
        'name': BeautifulSoup(str(ctf_html[0]),'lxml').text, 

        'link': ad2 + str(BeautifulSoup(str(ctf_html[0]),'lxml').a.get('href')), 

        'begin_date': str(BeautifulSoup(str(ctf_html[1]), 'lxml').text).split(' — ')[0].split(', ')[0][:6], 

        'begin_time': str(BeautifulSoup(str(ctf_html[1]), 'lxml').text).split(' — ')[0].split(', ')[1], 

        'end_date': str(BeautifulSoup(str(ctf_html[1]), 'lxml').text).split(' — ')[1].split(', ')[0][:-4][:6], 

        'end_time': str(BeautifulSoup(str(ctf_html[1]), 'lxml').text).split(' — ')[1].split(', ')[1],

        'type': BeautifulSoup(str(ctf_html[2]), 'lxml').text,

        'place': place_insert(BeautifulSoup(str(ctf_html[3]), 'lxml').text)
      }
      ctfs.append(ctf)

    for ctf in ctfs:
        existing_ctf = session.query(CTF).filter_by(name=ctf['name'], begin_date=ctf['begin_date']).first()
        if existing_ctf is None:
            new_ctf = CTF(**ctf)
            new_ctf.link = parse_links_from_page(new_ctf.link)
            session.add(new_ctf)
    session.commit()