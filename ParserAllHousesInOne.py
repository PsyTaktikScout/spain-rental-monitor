# +1. Idealista.com
# -2. Badi.com
# +3. fotocasa.es
# -4. pisocompartido.com

import os
import requests
import telebot
import time
import datetime
import csv
import locale
import json
import traceback
from datetime import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# pip install requests telebot time datetime csv locale
#print('-----Старт-----')


def take_all_posts_idealista():


       # 'if-none-match': 'W/"caa9cdacdabd723607e1acd282450146"',

    cookies = {
        'userUUID': 'f070439a-727a-4f56-a510-f121eb395c45',
        '_pprv': 'eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1rb2xkdGF0fG01MDZnYnl0In0%3D',
        '_pcid': '%7B%22browserId%22%3A%22m506gbyrtelt8kxp%22%2C%22_t%22%3A%22mkoldtgg%7Cm506gc4g%22%7D',
        '_pctx': '%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbANaVUrfAHN6AH34BWAAwA2cQGMALPRABfIA',
        '_fbp': 'fb.1.1734906361705.18678112912941123',
        '_tt_enable_cookie': '1',
        '_ttp': 'ZiNFls9B2vO53LO3EioAu9VT3XC.tt.1',
        '_gcl_au': '1.1.349859911.1734906380',
        '_last_search': 'interestZone',
        'askToSaveAlertPopUp': 'true',
        'sendbba8248e-a1b5-4184-9292-5c2610c8e4f7': '"{}"',
        'ABTasty': 'uid=ksk23ckb56sac7n7',
        'utag_main__prevCompleteClickName': '',
        '_clck': '1klp4yb%7C2%7Cfsw%7C0%7C1817',
        'contactdd163d74-a5f3-4206-a97a-363e3d1a902b': '"{\'maxNumberContactsAllow\':10}"',
        'SESSION': os.getenv('IDEALISTA_SESSION', '5a39a92ce6e23c79~dd163d74-a5f3-4206-a97a-363e3d1a902b'),
        'utag_main__sn': '4',
        'utag_main_ses_id': '1737910558444%3Bexp-session',
        'utag_main__prevTstitle': 'https%3A%2F%2Fwww.idealista.com%2Fru%2Fgeo%2Falquiler-viviendas%2Fcataluna%2Fcon-precio-hasta_850%2Cde-un-dormitorio%2Cde-dos-dormitorios%2Cde-tres-dormitorios%2Cde-cuatro-cinco-habitaciones-o-mas%2Cascensor%2Cbalcon-y-terraza%2Cpublicado_ultimas-24-horas%2Calquiler-de-larga-temporada%2F%3Fordenado-por%3Dfecha-publicacion-desc%3Bexp-1737914158620',
        'utag_main__prevTsReferrer': '%3Bexp-1737914158620',
        'utag_main__prevTsSource': 'Direct traffic%3Bexp-1737914158620',
        'utag_main__prevTsCampaign': 'organicTrafficByTm%3Bexp-1737914158620',
        'utag_main__prevTsProvider': '%3Bexp-1737914158620',
        'utag_main__ss': '0%3Bexp-session',
        'dicbo_id': '%7B%22dicbo_fetch%22%3A1737910564060%7D',
        'cookieSearch-1': '"/geo/alquiler-viviendas/cataluna/con-precio-hasta_850,de-un-dormitorio,de-dos-dormitorios,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,ascensor,balcon-y-terraza,publicado_ultimas-24-horas,alquiler-de-larga-temporada/:1737910796210"',
        'utag_main__pn': '3%3Bexp-session',
        'utag_main__se': '4%3Bexp-session',
        'utag_main__st': '1737912599909%3Bexp-session',
        'utag_main__prevCompletePageName': '005-idealista/portal > portal > viewResults%3Bexp-1737914400655',
        'utag_main__prevLevel2': '005-idealista/portal%3Bexp-1737914400655',
        '_uetsid': '78654930db6811ef9c2bafdc76f37f47',
        '_uetvid': '24831d70e4b611eebe4f7b46cfe223f5',
        'datadome': os.getenv('IDEALISTA_DATADOME', 'SpLzEuEG5rpGbFaeOhXBh8dKWuEB65LFxVUN6zzlvSt7VDOleZALVOnuHZXEKDB~n1gY36au0Bs442pmcNnvbPM8SQ9OYBvQkBa6LUnkOlrf69suAWRgDJKKkouH~0Hy'),
        '_clsk': 'nru3nf%7C1737910804656%7C5%7C0%7Cu.clarity.ms%2Fcollect',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'userUUID=f070439a-727a-4f56-a510-f121eb395c45; _pprv=eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6Im9wdC1pbiJ9LCIxIjp7Im1vZGUiOiJvcHQtaW4ifSwiMiI6eyJtb2RlIjoib3B0LWluIn0sIjMiOnsibW9kZSI6Im9wdC1pbiJ9LCI0Ijp7Im1vZGUiOiJvcHQtaW4ifSwiNSI6eyJtb2RlIjoib3B0LWluIn0sIjYiOnsibW9kZSI6Im9wdC1pbiJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjpudWxsLCJfdCI6Im1rb2xkdGF0fG01MDZnYnl0In0%3D; _pcid=%7B%22browserId%22%3A%22m506gbyrtelt8kxp%22%2C%22_t%22%3A%22mkoldtgg%7Cm506gc4g%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbANaVUrfAHN6AH34BWAAwA2cQGMALPRABfIA; _fbp=fb.1.1734906361705.18678112912941123; _tt_enable_cookie=1; _ttp=ZiNFls9B2vO53LO3EioAu9VT3XC.tt.1; _gcl_au=1.1.349859911.1734906380; _last_search=interestZone; askToSaveAlertPopUp=true; sendbba8248e-a1b5-4184-9292-5c2610c8e4f7="{}"; ABTasty=uid=ksk23ckb56sac7n7; utag_main__prevCompleteClickName=; _clck=1klp4yb%7C2%7Cfsw%7C0%7C1817; contactdd163d74-a5f3-4206-a97a-363e3d1a902b="{\'maxNumberContactsAllow\':10}"; SESSION=5a39a92ce6e23c79~dd163d74-a5f3-4206-a97a-363e3d1a902b; utag_main__sn=4; utag_main_ses_id=1737910558444%3Bexp-session; utag_main__prevTstitle=https%3A%2F%2Fwww.idealista.com%2Fru%2Fgeo%2Falquiler-viviendas%2Fcataluna%2Fcon-precio-hasta_850%2Cde-un-dormitorio%2Cde-dos-dormitorios%2Cde-tres-dormitorios%2Cde-cuatro-cinco-habitaciones-o-mas%2Cascensor%2Cbalcon-y-terraza%2Cpublicado_ultimas-24-horas%2Calquiler-de-larga-temporada%2F%3Fordenado-por%3Dfecha-publicacion-desc%3Bexp-1737914158620; utag_main__prevTsReferrer=%3Bexp-1737914158620; utag_main__prevTsSource=Direct traffic%3Bexp-1737914158620; utag_main__prevTsCampaign=organicTrafficByTm%3Bexp-1737914158620; utag_main__prevTsProvider=%3Bexp-1737914158620; utag_main__ss=0%3Bexp-session; dicbo_id=%7B%22dicbo_fetch%22%3A1737910564060%7D; cookieSearch-1="/geo/alquiler-viviendas/cataluna/con-precio-hasta_850,de-un-dormitorio,de-dos-dormitorios,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,ascensor,balcon-y-terraza,publicado_ultimas-24-horas,alquiler-de-larga-temporada/:1737910796210"; utag_main__pn=3%3Bexp-session; utag_main__se=4%3Bexp-session; utag_main__st=1737912599909%3Bexp-session; utag_main__prevCompletePageName=005-idealista/portal > portal > viewResults%3Bexp-1737914400655; utag_main__prevLevel2=005-idealista/portal%3Bexp-1737914400655; _uetsid=78654930db6811ef9c2bafdc76f37f47; _uetvid=24831d70e4b611eebe4f7b46cfe223f5; datadome=SpLzEuEG5rpGbFaeOhXBh8dKWuEB65LFxVUN6zzlvSt7VDOleZALVOnuHZXEKDB~n1gY36au0Bs442pmcNnvbPM8SQ9OYBvQkBa6LUnkOlrf69suAWRgDJKKkouH~0Hy; _clsk=nru3nf%7C1737910804656%7C5%7C0%7Cu.clarity.ms%2Fcollect',
        'priority': 'u=0, i',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.265", "Chromium";v="131.0.6778.265", "Not_A Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    params = {
        'ordenado-por': 'fecha-publicacion-desc',
    }

    response = requests.get(
        'https://www.idealista.com/ru/geo/alquiler-viviendas/cataluna/con-precio-hasta_850,de-un-dormitorio,de-dos-dormitorios,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,ascensor,balcon-y-terraza,publicado_ultimas-24-horas,alquiler-de-larga-temporada/',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    global status 
    status = response.status_code
    # print('(',str(status),')')
    # print('(',response.status_code,')')
    # print(response.json()['data']['results'])
    # print('==================================')

    l=[]
    o={}

    soup = BeautifulSoup(response.text, 'html.parser')

    allProperties = soup.find_all("div",{"class":"item-info-container"})

    for i in range(0,len(allProperties)):
        o["price"]=allProperties[i].find("span",{"class":"item-price"}).text.strip("\n")
        vez=0
        o['area-size']=''
        for area in allProperties[i].find_all("span",{"class":"item-detail"}):
            if vez<3:
                o["area-size"]=o['area-size']+ area.text.strip("\n")+"\n"
            vez=vez+1
        # for area in allProperties[i].find_all("span",{"class":"item-detail"}):
        #     print('\n------area------\n')
        #     print(area.text.strip("\n"))
        #     print('\n-------area------END\n')
        o["title"]=allProperties[i].find("a",{"class":"item-link"}).text.strip("\n") #+ allProperties[i].find("div",{"class":"item-description"}).text.strip("\n")
        o["property-link"]="https://www.idealista.com"+allProperties[i].find("a",{"class":"item-link"}).get('href')
        l.append(o)
        o={}



    # print("\n-------- вернул сайт -----------\n")
    # print(l)
    # print("\n-------- вернул сайт -----------конец\n")

    return l

def file_writer_idealista(data):
# Записываем строки в новый CSV файл
    fieldnames = data[0].keys()
    with open('idealista.csv', 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)

def file_writer_new_idealista(data):
    # print("\n-------- data -----------\n")
    # print(data)
    # print("\n-------- data -----------конец\n")

#    now = datetime.datetime.now()
#    with open(domain+'_'+now.strftime("%Y-%m-%d_%H%M")+'.csv', 'w') as file:
    with open('idealista_new.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('price','area-size','title','property-link'))
        for item in data:
            # print("\n-------- item in data -----------\n")
            # print(item)
            # print("\n-------- item in data -----------конец\n")
            a_pen.writerow((item['price'],item['area-size'],item['title'],item['property-link']))

def file_writer_for_error_idealista(data):
#    now = datetime.datetime.now()
#    with open(domain+'_'+now.strftime("%Y-%m-%d_%H%M")+'.csv', 'w') as file:
    with open('idealista.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('price','area-size','title','property-link'))
        for item in data:
            # print("\n-------- item in data for error -----------\n")
            # print(item)
            # print("\n-------- item in data -----------конец\n")
            a_pen.writerow((item['price'],item['area-size'],item['title'],item['property-link']))
    # exit()

def file_reader_idealista():
    data = []
    with open('idealista.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def file_reader_new_idealista():
    data = []
    with open('idealista_new.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def new_tasks_t_message_idealista(mesage_rows):
    
    global bot
    global chat_id
    text_m=''
    iskluchit=[
        'еpепeчатать рyкoписный тeкcт'
               ]
    razreshen=1
    for row in mesage_rows:
        for int in iskluchit:
            if int in row['title']:
                razreshen=0
                print(' -X-', end=" ")    
        if razreshen>0:     #'price','area-size','title','property-link'
            text_m=text_m+str(row['price'])+'\n'+str(row['area-size'])+'\n'+str(row['title'])+'\n'+str(row['property-link'])+'\n'+'\n'
    
    # Разбиваем длинное сообщение на более короткие
    max_length = 4000  # Максимальная длина одного сообщения
    chunks = [text_m[i:i+max_length] for i in range(0, len(text_m), max_length)]

    for chunk in chunks:
        bot.send_message(chat_id, chunk)

def start_idealista():
    firstStartAll=0
    global status

    global token  # токен телеграм бота
    global bot
    global chat_id  # Например chat_id = '223344'   

    # while True:
    try:

        # bot.send_message(chat_id, 'TEST')
        # exit()
        print('Idealista:   Вост+', end="|") 
        old_posts = file_reader_idealista()
        # print('old_posts\n')
        # print('old_posts\n')
        # print('old_posts\n')
        # print(old_posts)
        # print('old_posts_END\n')
        print('Загр+', end="|") 
        all_posts = take_all_posts_idealista()
        # print("\n-------- получил вернул сайт -----------\n")
        # print(all_posts)
        # print("\n-------- получил вернул сайт -----------конец\n")
        print('Новые+', end="|") 
        file_writer_new_idealista(all_posts)
        all_posts = file_reader_new_idealista() # Читаем из файла, для конвертации данных в нужный формат
        # print('all_posts\n')
        # print('all_posts\n')
        # print('all_posts\n')
        # print(all_posts)
        # print('all_posts_END\n')
        print('Новые+', end="|") 
        unique_rows = [row for row in all_posts if row not in old_posts]
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print(unique_rows)
        # print('unique_rows_END\n')
        print('Собщение+', end="|") 

        new_tasks_t_message_idealista(unique_rows)
    
        all_posts = old_posts + unique_rows
        print('Сохр+', end="|")
        file_writer_idealista(all_posts)
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('ВсеОК ', formatted_time)
        # exit()
        # time.sleep(3*60)
    except FileNotFoundError as e:
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print("Произошла ошибка:", e,' Исправляем.', formatted_time)
        all_posts = take_all_posts_idealista()
        file_writer_for_error_idealista(all_posts)

        #----------------- try --------------------------------
        # bot.send_message(chat_id, 'TEST')
        # exit()
        print('Idealista:   Вост+', end="|") 
        old_posts = file_reader_idealista()
        # print('old_posts\n')
        # print('old_posts\n')
        # print('old_posts\n')
        # print(old_posts)
        # print('old_posts_END\n')
        print('Загр+', end="|") 
        all_posts = take_all_posts_idealista()
        # print("\n-------- получил вернул сайт -----------\n")
        # print(all_posts)
        # print("\n-------- получил вернул сайт -----------конец\n")
        print('Новые+', end="|") 
        file_writer_new_idealista(all_posts)
        all_posts = file_reader_new_idealista() # Читаем из файла, для конвертации данных в нужный формат
        # print('all_posts\n')
        # print('all_posts\n')
        # print('all_posts\n')
        # print(all_posts)
        # print('all_posts_END\n')
        print('Новые+', end="|") 
        unique_rows = [row for row in all_posts if row not in old_posts]
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print(unique_rows)
        # print('unique_rows_END\n')
        print('Собщение+', end="|") 

        new_tasks_t_message_idealista(unique_rows)
    
        all_posts = old_posts + unique_rows
        print('Сохр+', end="|")
        file_writer_idealista(all_posts)
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('ВсеОК ', formatted_time)
        # exit()
        # time.sleep(3*60)
        #------------------------try end-----------------------------------
    except Exception as e:
        # Обработка других исключений
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('\n','-'*50,'\n\n',traceback.format_exc(),'\n\n','='*50,'\n')  # Выведет всю трассировку ошибки
        print("Произошла ошибка:", e,' Рестарт через 3 мин.(',status,')   ', formatted_time)
        s_mes="Idealista:"+ str(e)+'|Р:3м('+str(status)+')'+ str(formatted_time)
        print(s_mes)
        bot.send_message(chat_id, s_mes)

        # exit()
        time.sleep(5)


def take_all_posts_badi():


    headers = {
        'accept': 'application/json',
        'accept-language': 'es-ES',
        'authorization': f'Bearer {os.getenv("BADI_BEARER_TOKEN")}',
        'badi-app-version': '5.123.6',
        'badi-device-id': 'f003c23c-c266-4961-a233-ed833c77506b',
        'badi-favourite-language': 'ru-RU, ru, en-US, en',
        'badi-inner-window-size': '428x904',
        'badi-language': 'es-ES',
        'badi-os-version': 'OS X 10.15.7 64-bit',
        'badi-platform': 'web',
        'badi-screen-size': '1680x1050',
        'content-type': 'application/json',
       # 'if-none-match': 'W/"caa9cdacdabd723607e1acd282450146"',
        'origin': 'https://badi.com',
        'priority': 'u=1, i',
        'referer': 'https://badi.com/',
        'search-source': 'search-bar',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://api.badiapp.com/v1/application/search/rooms?page=1&per=20&price_types[]=3&bounds[ne][lat]=42.861439&bounds[ne][lng]=3.3325539&bounds[sw][lat]=40.5230466&bounds[sw][lng]=0.1590702&sort_by=recent&max_price=850&length_of_stay[]=long&place_types[]=2',
        headers=headers,
    )

    global status
    status = response.status_code
    # print('(',str(status),')')
    # print(response.status_code, end="-------------------------")
    # print(response.json()['data']['results'])
    # print('==================================')
    # raise PermissionError("test error")



    # count = 0              # индекс с номером страницы
    # page = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']              # начало
    # maxCount = 1          # конец
    all_posts = []

    # while count < maxCount:
    #     response = requests.get('https://kabanchik.ua/ua/cabinet/recommended',
    #                             params={
    #                                 'page': page[count],
    #                                 'category': ''
    #                             },
    #                             cookies=cookies, 
    #                             headers=headers)

    #     data = response.json()['items']
    data = response.json()['data']['results']
    #     count += 1
    #     maxCount = response.json()['pages']
    #     all_posts.extend(data)
    all_posts.extend(data)
    # print(all_posts[0])
    # print('----------all_posts-----------')
    #     print(str(count)+'/'+str(maxCount), end=" ")
    #     time.sleep(0.5)
    # filtred_post = []
    filtred_post = []
    # for row in all_posts:
    #     filtred_post.append((row['id'],
    #                         locale.str(row['cost']),
    #                         row['title'],
    #                         row['datetime_due'], data.results[0].attributes.extra_info[1].body.content
    #                         row['status_title'],
    #                         row['url']))
    # return filtred_post
    for row in all_posts:
#        print(row['attributes']['extra_info'][0]['body']['content'])
        filtred_post.append((row['attributes']['subheading']['content'], # Площадь
                            row['attributes']['marker']['label']['content'], # Цена
                     #       row['attributes']['extra_info'][1]['body']['content'], # Включены ли куммунальные
                            'https://badi.com/es/room/' + str(row['attributes']['room_id']), # room_id
                            'https://www.google.com/maps?q=' + str(row['attributes']['marker']['lat']) + ',' + str(row['attributes']['marker']['lng'])))
    # print(filtred_post)
    # print('---------------------------')
    return filtred_post

def file_writer_badi(data):
# Записываем строки в новый CSV файл
    fieldnames = data[0].keys()
    with open('badi.csv', 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)

def file_writer_new_badi(data):
#    now = datetime.datetime.now()
#    with open(domain+'_'+now.strftime("%Y-%m-%d_%H%M")+'.csv', 'w') as file:
    with open('badi_new.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('M2','Price','url','Map'))
        for item in data:

            a_pen.writerow(item)

def file_writer_for_error_badi(data):
#    now = datetime.datetime.now()
#    with open(domain+'_'+now.strftime("%Y-%m-%d_%H%M")+'.csv', 'w') as file:
    with open('badi.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('M2','Price','url','Map'))
        for item in data:

            a_pen.writerow(item)

def file_reader_badi():
    data = []
    with open('badi.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def file_reader_new_badi():
    data = []
    with open('badi_new.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def new_tasks_t_message_badi(mesage_rows):
    
    global bot
    global chat_id
    text_m=''
    iskluchit=[
        'COMPAÑEROS DE PISO'
               ]
    razreshen=1
    for row in mesage_rows:
        for int in iskluchit:
            if int in row['url']:
                razreshen=0
                print(' -X-', end=" ")    
        if razreshen>0:     #'M2','Price','url','Map'
            text_m=text_m+str(row['M2'])+'\n'+str(row['Price'])+'\n'+str(row['url'])+'\n'+str(row['Map'])+'\n'+'\n'
    # print('text_m\n')
    # print('text_m\n')
    # print('text_m\n')
    # print(text_m)
    # print('text_m_END\n')
    
    # Разбиваем длинное сообщение на более короткие
    max_length = 4000  # Максимальная длина одного сообщения
    chunks = [text_m[i:i+max_length] for i in range(0, len(text_m), max_length)]

    # Отправляем части сообщения последовательно
    #chat_id = 'USER_CHAT_ID'  # Замени на реальный идентификатор чата

    for chunk in chunks:
        bot.send_message(chat_id, chunk)




    # bot.send_message(chat_id, text=text_m)

def start_badi(): 
    firstStartAll = 0
    global status

    global token
    global bot
    global chat_id

    try:
        #bot.send_message(chat_id, 'TEST')
        print('Badi:   Вост+', end="|") 
        # exit()
        # raise PermissionError("test error")
        old_posts = file_reader_badi()
        # print('old_posts\n')
        # print('old_posts\n')
        # print('old_posts\n')
        # print(old_posts)
        # print('old_posts_END\n')
        print('Загр+', end="|") 
        all_posts = take_all_posts_badi()
        # raise PermissionError("test error")
        # print('all_posts1\n')
        # print('all_posts1\n')
        # print('all_posts1\n')
        # print(all_posts)
        # print('all_posts1_END\n')
        print('Новые+', end="|") 
        file_writer_new_badi(all_posts)
        all_posts = file_reader_new_badi() # Читаем из файла, для конвертации данных в нужный формат
        # print('all_posts\n')
        # print('all_posts\n')
        # print('all_posts\n')
        # print(all_posts)
        # print('all_posts_END\n')
        print('Новые+', end="|") 
        unique_rows = [row for row in all_posts if row not in old_posts]
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print(unique_rows)
        # print('unique_rows_END\n')
        print('Собщение+', end="|") 

        new_tasks_t_message_badi(unique_rows)
    
        all_posts = old_posts + unique_rows
        print('Сохр+', end="|")
        file_writer_badi(all_posts)
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('ВсеОК ', formatted_time)
        # time.sleep(3*60)
    except FileNotFoundError as e:
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print("Произошла ошибка:", e,' Исправляем.', formatted_time)
        all_posts = take_all_posts_badi()
        file_writer_for_error_badi(all_posts)
        #-----------------------------try--------------------------
        #bot.send_message(chat_id, 'TEST')
        print('Badi:   Вост+', end="|") 
        # exit()
        # raise PermissionError("test error")
        old_posts = file_reader_badi()
        # print('old_posts\n')
        # print('old_posts\n')
        # print('old_posts\n')
        # print(old_posts)
        # print('old_posts_END\n')
        print('Загр+', end="|") 
        all_posts = take_all_posts_badi()
        # raise PermissionError("test error")
        # print('all_posts1\n')
        # print('all_posts1\n')
        # print('all_posts1\n')
        # print(all_posts)
        # print('all_posts1_END\n')
        print('Новые+', end="|") 
        file_writer_new_badi(all_posts)
        all_posts = file_reader_new_badi() # Читаем из файла, для конвертации данных в нужный формат
        # print('all_posts\n')
        # print('all_posts\n')
        # print('all_posts\n')
        # print(all_posts)
        # print('all_posts_END\n')
        print('Новые+', end="|") 
        unique_rows = [row for row in all_posts if row not in old_posts]
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print(unique_rows)
        # print('unique_rows_END\n')
        print('Собщение+', end="|") 

        new_tasks_t_message_badi(unique_rows)
    
        all_posts = old_posts + unique_rows
        print('Сохр+', end="|")
        file_writer_badi(all_posts)
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('ВсеОК ', formatted_time)
        # time.sleep(3*60)
        #-----------------------------try end----------------------
    except Exception as e:
        # Обработка других исключений
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('\n','-'*50,'\n\n',traceback.format_exc(),'\n\n','='*50,'\n')  # Выведет всю трассировку ошибки
        print("Произошла ошибка:", e,' Рестарт через 5 секунд.', formatted_time)
        # exit()
        s_mes="Badi:"+ str(e)+'|Р:3м('+str(status)+')'+ str(formatted_time)
        print(s_mes)
        bot.send_message(chat_id, s_mes)

        time.sleep(5)



def take_all_posts_fotocasa():
    # headers = {
       # 'if-none-match': 'W/"caa9cdacdabd723607e1acd282450146"',

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://www.fotocasa.es',
        'priority': 'u=1, i',
        'referer': 'https://www.fotocasa.es/',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://web.gw.fotocasa.es/v2/propertysearch/search/propertycoordinates?combinedLocationIds=724,9,8,0,0,0,0,0,0&culture=es-ES&featureIds=13&includePurchaseTypeFacets=false&isMap=false&isNewConstructionPromotions=false&latitude=41.3829&longitude=2.17704&maxPrice=850&minRooms=2&pageNumber=1&platformId=1&propertyTypeId=2&publicationDate=TWO_DAYS&size=300&sortOrderDesc=true&sortType=publicationDate&transactionTypeId=3',
        headers=headers,
    )


    global status
    status = response.status_code
    # print('(',str(status),')')
    # print(response.status_code, end="-------------------------")
    # print(response.json()['data']['results'])
    # print('==================================')
    # raise PermissionError("test error")
    # exit()



    # count = 0              # индекс с номером страницы
    # page = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']              # начало
    # maxCount = 1          # конец
    all_posts = []

    # while count < maxCount:
    #     response = requests.get('https://kabanchik.ua/ua/cabinet/recommended',
    #                             params={
    #                                 'page': page[count],
    #                                 'category': ''
    #                             },
    #                             cookies=cookies, 
    #                             headers=headers)

    #     data = response.json()['items']
    # print('\n\n',response.json()['propertyCoordinates'])
    data = response.json()['propertyCoordinates']
    #     count += 1
    #     maxCount = response.json()['pages']
    #     all_posts.extend(data)
    all_posts.extend(data)
    # print('\n\n',all_posts[0])
    # exit()
    # print('----------all_posts-----------')
    #     print(str(count)+'/'+str(maxCount), end=" ")
    #     time.sleep(0.5)
    # filtred_post = []
    filtred_post = []
    # for row in all_posts:
    #     filtred_post.append((row['id'],
    #                         locale.str(row['cost']),
    #                         row['title'],
    #                         row['datetime_due'], data.results[0].attributes.extra_info[1].body.content
    #                         row['status_title'],
    #                         row['url']))
    # return filtred_post  
    for row in all_posts:
        try:
            rooms = '?'
            surface = '-'
            terrace = '-'
            balcony = '-'
            price = '?'
            propertyId = ''
            room_url = ''
            room_map = ''
            latitude=''
            longitude=''

            price=str(row['price'])
            propertyId=str(row['propertyId'])
            latitude=str(row['coordinates']['latitude'])
            longitude=str(row['coordinates']['longitude'])
            room_url='https://www.fotocasa.es/es/alquiler/0/0/0/'+propertyId+'/d?from=list'
            room_map='https://www.google.com/maps?q=' + latitude + ',' + longitude

            # print(price,'price\n',
            # propertyId,'propertyId\n',
            # latitude,'latitude\n',
            # longitude,'longitude\n')

            for item in row['features']:
                # print('\n\n',item['key'])
                if item['key'] == 'rooms':
                    # print(' - ',item['value'][0])
                    rooms=str(item['value'][0])
                if item['key'] == 'surface':
                    # print(' - ',item['value'][0])
                    surface=str(item['value'][0])
                if item['key'] == 'terrace':
                    # print(' - ',item['value'][0])
                    terrace=str(item['value'][0])
                if item['key'] == 'balcony':
                    # print(' - ',item['value'][0])
                    balcony=str(item['value'][0])
    #        print(row['attributes']['extra_info'][0]['body']['content'])
            filtred_post.append(('rooms: '+rooms+' ('+surface+' m2)', # Площадь
                                'price: '+price+' (t'+terrace+',b'+balcony+')', # Цена
                        #       row['attributes']['extra_info'][1]['body']['content'], # Включены ли куммунальные
                                room_url, # room_id
                                room_map))
        except Exception as e:
            print('\n','-'*50,'\n\n',traceback.format_exc(),'\n\n','='*50,'\n')  # Выведет всю трассировку ошибки
            print('')
    # print(filtred_post)
    # print('---------------------------')
    # exit()
    return filtred_post

def file_writer_fotocasa(data):
# Записываем строки в новый CSV файл
    fieldnames = data[0].keys()
    with open('fotocasa.csv', 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)

def file_writer_new_fotocasa(data):
#    now = datetime.datetime.now()
#    with open(domain+'_'+now.strftime("%Y-%m-%d_%H%M")+'.csv', 'w') as file:
    with open('fotocasa_new.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('M2','Price','url','Map'))
        for item in data:

            a_pen.writerow(item)

def file_writer_for_error_fotocasa(data):
#    now = datetime.datetime.now()
#    with open(domain+'_'+now.strftime("%Y-%m-%d_%H%M")+'.csv', 'w') as file:
    with open('fotocasa.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('M2','Price','url','Map'))
        for item in data:

            a_pen.writerow(item)

def file_reader_fotocasa():
    data = []
    with open('fotocasa.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def file_reader_new_fotocasa():
    data = []
    with open('fotocasa_new.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def new_tasks_t_message_fotocasa(mesage_rows):
    
    global bot
    global chat_id
    text_m=''
    iskluchit=[
        'еpепeчатать рyкoписный тeкcт'
               ]
    razreshen=1
    for row in mesage_rows:
        for int in iskluchit:
            if int in row['url']:
                razreshen=0
                print(' -X-', end=" ")    
        if razreshen>0:     #'M2','Price','url','Map'
            text_m=text_m+str(row['M2'])+'\n'+str(row['Price'])+'\n'+str(row['url'])+'\n'+str(row['Map'])+'\n'+'\n'
    # print('text_m\n')
    # print('text_m\n')
    # print('text_m\n')
    # print(text_m)
    # print('text_m_END\n')
    
    # Разбиваем длинное сообщение на более короткие
    max_length = 4000  # Максимальная длина одного сообщения
    chunks = [text_m[i:i+max_length] for i in range(0, len(text_m), max_length)]

    # Отправляем части сообщения последовательно
    #chat_id = 'USER_CHAT_ID'  # Замени на реальный идентификатор чата

    for chunk in chunks:
        bot.send_message(chat_id, chunk)




    # bot.send_message(chat_id, text=text_m)

def start_fotocasa(): 
    firstStartAll = 0
    global status

    global token
    global bot
    global chat_id

    try:
        #bot.send_message(chat_id, 'TEST')
        print('fotocasa:   Вост+', end="|") 
        # exit()
        # raise PermissionError("test error")
        old_posts = file_reader_fotocasa()
        # print('old_posts\n')
        # print('old_posts\n')
        # print('old_posts\n')
        # print(old_posts)
        # print('old_posts_END\n')
        print('Загр+', end="|") 
        all_posts = take_all_posts_fotocasa()
        # raise PermissionError("test error")
        # print('all_posts1\n')
        # print('all_posts1\n')
        # print('all_posts1\n')
        # print(all_posts)
        # print('all_posts1_END\n')
        print('Новые+', end="|") 
        file_writer_new_fotocasa(all_posts)
        all_posts = file_reader_new_fotocasa() # Читаем из файла, для конвертации данных в нужный формат
        # print('all_posts\n')
        # print('all_posts\n')
        # print('all_posts\n')
        # print(all_posts)
        # print('all_posts_END\n')
        print('Новые+', end="|") 
        unique_rows = [row for row in all_posts if row not in old_posts]
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print(unique_rows)
        # print('unique_rows_END\n')
        print('Собщение+', end="|") 

        new_tasks_t_message_fotocasa(unique_rows)
    
        all_posts = old_posts + unique_rows
        print('Сохр+', end="|")
        file_writer_fotocasa(all_posts)
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('ВсеОК ', formatted_time)
        # time.sleep(3*60)
    except FileNotFoundError as e:
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print("Произошла ошибка:", e,' Исправляем.', formatted_time)
        all_posts = take_all_posts_fotocasa()
        file_writer_for_error_fotocasa(all_posts)
        #-----------------------------try--------------------------
        #bot.send_message(chat_id, 'TEST')
        print('fotocasa:   Вост+', end="|") 
        # exit()
        # raise PermissionError("test error")
        old_posts = file_reader_fotocasa()
        # print('old_posts\n')
        # print('old_posts\n')
        # print('old_posts\n')
        # print(old_posts)
        # print('old_posts_END\n')
        print('Загр+', end="|") 
        all_posts = take_all_posts_fotocasa()
        # raise PermissionError("test error")
        # print('all_posts1\n')
        # print('all_posts1\n')
        # print('all_posts1\n')
        # print(all_posts)
        # print('all_posts1_END\n')
        print('Новые+', end="|") 
        file_writer_new_fotocasa(all_posts)
        all_posts = file_reader_new_fotocasa() # Читаем из файла, для конвертации данных в нужный формат
        # print('all_posts\n')
        # print('all_posts\n')
        # print('all_posts\n')
        # print(all_posts)
        # print('all_posts_END\n')
        print('Новые+', end="|") 
        unique_rows = [row for row in all_posts if row not in old_posts]
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print(unique_rows)
        # print('unique_rows_END\n')
        print('Собщение+', end="|") 

        new_tasks_t_message_fotocasa(unique_rows)
    
        all_posts = old_posts + unique_rows
        print('Сохр+', end="|")
        file_writer_fotocasa(all_posts)
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('ВсеОК ', formatted_time)
        # time.sleep(3*60)
        #-----------------------------try end----------------------
    except Exception as e:
        # Обработка других исключений
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('\n','-'*50,'\n\n',traceback.format_exc(),'\n\n','='*50,'\n')  # Выведет всю трассировку ошибки
        print("Произошла ошибка:", e,' Рестарт через 5 секунд.', formatted_time)
        # exit()
        s_mes="fotocasa:"+ str(e)+'|Р:3м('+str(status)+')'+ str(formatted_time)
        print(s_mes)
        bot.send_message(chat_id, s_mes)

        # time.sleep(3*60)




def take_all_posts_pisocompartido():

       # 'if-none-match': 'W/"caa9cdacdabd723607e1acd282450146"',
    
    import requests

    cookies = {
        'PHPSESSID': os.getenv('PISO_PHPSESSID', '3662962036a43b6405ee8c931cfaa675'),
        'piso_lang': 'es',
        'AMCVS_9854C13E58403FEB0A495D53%40AdobeOrg': '1',
        '_ga': 'GA1.1.1371456446.1739154764',
        '_clck': '1bj6qqg%7C2%7Cftb%7C0%7C1867',
        's_ecid': 'MCMID%7C13408647863159457050490538892132299535',
        's_cc': 'true',
        'AMCV_9854C13E58403FEB0A495D53%40AdobeOrg': '179643557%7CMCIDTS%7C20130%7CMCMID%7C13408647863159457050490538892132299535%7CMCAAMLH-1739759563%7C6%7CMCAAMB-1739759563%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1739161964s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-20137%7CvVersion%7C5.5.0',
        'G_ENABLED_IDPS': 'google',
        'didomi_token': 'eyJ1c2VyX2lkIjoiMTk0ZWRiM2EtNjdlYy02ODg5LWEyNTAtNDFlYTdiYjRiZDVjIiwiY3JlYXRlZCI6IjIwMjUtMDItMTBUMDI6MzI6NDEuMzQyWiIsInVwZGF0ZWQiOiIyMDI1LTAyLTEwVDAyOjMyOjQ3LjI3MFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYW1hem9uIiwidHdpdHRlciIsImM6aW5kaWdpdGFsbC1QM0Y0aWZXNCIsImM6dmlkZW9sb2d5IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOnBlbmR1bGFyLU1mZ2tCZEFlIl19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkRPdUJBQUVZQUxJQWJBQmlBR0tBUE1BOVVDSWdFU1FJcGdTaUFtY0JhQURDd0dNQU02Z2NTQTVRQ0JnRWhnSnpnVm5ndEdCYVNDNTBGMVFNT0lZbkJpZURHNEdPSU0zQVoxZ0EuRE91QkFBRVlBTElBYkFCaUFHS0FQTUE5VUNJZ0VTUUlwZ1NpQW1jQmFBREN3R01BTTZnY1NBNVFDQmdFaGdKemdWbmd0R0JhU0M1MEYxUU1PSVluQmllREc0R09JTTNBWjFnQSJ9',
        'euconsent-v2': 'CQMnI8AQMnI8AAHABBENBbFsAP_gAEPgAAiQJkNX_G__bWlr8X73aftkeY1P99h77sQxBhbJE-4FzLvW_JwXx2E5NAz6tqIKmRIAu3TBIQNlHJDURVCgaogVrSDMaEyUoTNKJ6BkiFMRI2dYCFxvm4tjeQCY5vr991dx2B-t7dr83dzyy4hHn3a5_2S0WJCdA4-tDev9bROb-9IOd_x8v4v4_F7pE2_eT1l_tWvp7D9-cts_9XQTFAJMNCogDLAkJCDQMIIEAKgrCAigQBAAAkDRAQAmDAp2BgAusJEAIAUAAwQAgABBkACAAACABCIAIACgQAAQCBQABgAQCAQAEDAACACwEAgABAdAxTAggECwASMyKhTAhAASCAlsqEEgCBBXCEIs8AiAREwUAAAAABSAAICwWBxJICVCQQBcQTQAAEACAQQAFCCTkwABAGbLUAAA.f_wACHwAAAAA',
        'sui_1pc': '17391547673241A7847DBB545F93D1D7056A26552ADFAF84B3CFEBC8',
        'Y3djb25zZW50': '1',
        '_clsk': '1ij0s4h%7C1739155358908%7C3%7C1%7Cv.clarity.ms%2Fcollect',
        's_nr': '1739155367747-New',
        's_ppn': 'piso%3A1148286%3Apisos-en-carrer-esteve-terrades-granollers-por-796%E2%82%AC-al-mes',
        '_ga_HLGVJV0DKB': 'GS1.1.1739154763.1.1.1739155368.0.0.0',
        's_ppvl': 'piso%253A1148286%253Apisos-en-carrer-esteve-terrades-granollers-por-796%25u20AC-al-mes%2C27%2C27%2C941%2C1680%2C904%2C1680%2C1050%2C2%2CP',
        's_ppv': 'pisos-barcelona%253Ahasta-850%253Ahabitaciones-2%253Aalquiler-de-pisos-en-barcelona%2C35%2C35%2C904%2C428%2C904%2C1680%2C1050%2C2%2CL',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'PHPSESSID=3662962036a43b6405ee8c931cfaa675; piso_lang=es; AMCVS_9854C13E58403FEB0A495D53%40AdobeOrg=1; _ga=GA1.1.1371456446.1739154764; _clck=1bj6qqg%7C2%7Cftb%7C0%7C1867; s_ecid=MCMID%7C13408647863159457050490538892132299535; s_cc=true; AMCV_9854C13E58403FEB0A495D53%40AdobeOrg=179643557%7CMCIDTS%7C20130%7CMCMID%7C13408647863159457050490538892132299535%7CMCAAMLH-1739759563%7C6%7CMCAAMB-1739759563%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1739161964s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-20137%7CvVersion%7C5.5.0; G_ENABLED_IDPS=google; didomi_token=eyJ1c2VyX2lkIjoiMTk0ZWRiM2EtNjdlYy02ODg5LWEyNTAtNDFlYTdiYjRiZDVjIiwiY3JlYXRlZCI6IjIwMjUtMDItMTBUMDI6MzI6NDEuMzQyWiIsInVwZGF0ZWQiOiIyMDI1LTAyLTEwVDAyOjMyOjQ3LjI3MFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYW1hem9uIiwidHdpdHRlciIsImM6aW5kaWdpdGFsbC1QM0Y0aWZXNCIsImM6dmlkZW9sb2d5IiwiYzpnb29nbGVhbmEtNFRYbkppZ1IiLCJjOnBlbmR1bGFyLU1mZ2tCZEFlIl19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkRPdUJBQUVZQUxJQWJBQmlBR0tBUE1BOVVDSWdFU1FJcGdTaUFtY0JhQURDd0dNQU02Z2NTQTVRQ0JnRWhnSnpnVm5ndEdCYVNDNTBGMVFNT0lZbkJpZURHNEdPSU0zQVoxZ0EuRE91QkFBRVlBTElBYkFCaUFHS0FQTUE5VUNJZ0VTUUlwZ1NpQW1jQmFBREN3R01BTTZnY1NBNVFDQmdFaGdKemdWbmd0R0JhU0M1MEYxUU1PSVluQmllREc0R09JTTNBWjFnQSJ9; euconsent-v2=CQMnI8AQMnI8AAHABBENBbFsAP_gAEPgAAiQJkNX_G__bWlr8X73aftkeY1P99h77sQxBhbJE-4FzLvW_JwXx2E5NAz6tqIKmRIAu3TBIQNlHJDURVCgaogVrSDMaEyUoTNKJ6BkiFMRI2dYCFxvm4tjeQCY5vr991dx2B-t7dr83dzyy4hHn3a5_2S0WJCdA4-tDev9bROb-9IOd_x8v4v4_F7pE2_eT1l_tWvp7D9-cts_9XQTFAJMNCogDLAkJCDQMIIEAKgrCAigQBAAAkDRAQAmDAp2BgAusJEAIAUAAwQAgABBkACAAACABCIAIACgQAAQCBQABgAQCAQAEDAACACwEAgABAdAxTAggECwASMyKhTAhAASCAlsqEEgCBBXCEIs8AiAREwUAAAAABSAAICwWBxJICVCQQBcQTQAAEACAQQAFCCTkwABAGbLUAAA.f_wACHwAAAAA; sui_1pc=17391547673241A7847DBB545F93D1D7056A26552ADFAF84B3CFEBC8; Y3djb25zZW50=1; _clsk=1ij0s4h%7C1739155358908%7C3%7C1%7Cv.clarity.ms%2Fcollect; s_nr=1739155367747-New; s_ppn=piso%3A1148286%3Apisos-en-carrer-esteve-terrades-granollers-por-796%E2%82%AC-al-mes; _ga_HLGVJV0DKB=GS1.1.1739154763.1.1.1739155368.0.0.0; s_ppvl=piso%253A1148286%253Apisos-en-carrer-esteve-terrades-granollers-por-796%25u20AC-al-mes%2C27%2C27%2C941%2C1680%2C904%2C1680%2C1050%2C2%2CP; s_ppv=pisos-barcelona%253Ahasta-850%253Ahabitaciones-2%253Aalquiler-de-pisos-en-barcelona%2C35%2C35%2C904%2C428%2C904%2C1680%2C1050%2C2%2CL',
        'priority': 'u=0, i',
        'referer': 'https://www.pisocompartido.com/habitaciones-barcelona/?orden=9',
        'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    }

    params = {
        'tipo_alquiler': 'residencial',
        'select_provincia': 'barcelona.P00000000000008',
        'select_municipio': '',
        'select_distrito': '',
        'select_barrio': '',
        'ch_hab': '0',
        'ch_piso': '1',
        'precio': '850',
        'total_habs': '2',
        'banos': '',
    }

    response = requests.get(
        'https://www.pisocompartido.com/pisos-barcelona/hasta-850/habitaciones-2/',
        params=params,
        cookies=cookies,
        headers=headers,
    )


    global status 
    status = response.status_code
    # print('(',str(status),')')
    # print(response.json()['data']['results'])
    # print('==================================')
    # exit()
    l=[]
    o={}

    soup = BeautifulSoup(response.text, 'html.parser')

    allProperties = soup.find_all("script",{"type":"application/ld+json"})
    


    for script in allProperties:
        try:
            # print(script)
            # data = json.loads(script.string)  # Преобразуем JSON в словарь

            json_text = script.string.strip()  # Извлекаем содержимое скрипта и убираем лишние пробелы
            # print(json_text)
            data = json.loads(json_text, strict=False)  # Декодируем JSON
            # print(data)

            name=None
            price=None
            url=None
            latitude=None
            longitude=None
            temp=None

            # Проверяем, если данные хранятся в "@graph"
            if "@graph" in data:
                for item in data["@graph"]:
                    temp=item.get("name")
                    if temp!=None:
                        name = item.get("name")
                    temp=item.get("offers", {}).get("price")
                    if temp!=None:
                        price = item.get("offers", {}).get("price")
                    temp=item.get("offers", {}).get("url")
                    if temp!=None:
                        url = item.get("offers", {}).get("url")
                    temp=item.get("geo", {}).get("latitude")
                    if temp!=None:
                        latitude = item.get("geo", {}).get("latitude")
                    temp=item.get("geo", {}).get("longitude")
                    if temp!=None:
                        longitude = item.get("geo", {}).get("longitude")

            # print(f"Название: {name}")
            # print(f"Цена: {price}")
            # print(f"URL: {url}")
            # print(f"Широта: {latitude}")
            # print(f"Долгота: {longitude}")
            # print("-" * 50)

            l.append((price,url,name,'https://www.google.com/maps?q=' + latitude + ',' + longitude))

        except Exception as e:
            print('\n','-'*50,'\n\n',traceback.format_exc(),'\n\n','='*50,'\n')  # Выведет всю трассировку ошибки
            print('\n\nне работает: ',e)
    #         exit()
    # print(l)
    # exit()


    # for i in range(0,len(allProperties)):
    #     o["price"]=allProperties[i].find("span",{"class":"item-price"}).text.strip("\n")
    #     vez=0
    #     o['area-size']=''
    #     for area in allProperties[i].find_all("span",{"class":"item-detail"}):
    #         if vez<3:
    #             o["area-size"]=o['area-size']+ area.text.strip("\n")+"\n"
    #         vez=vez+1
    #     # for area in allProperties[i].find_all("span",{"class":"item-detail"}):
    #     #     print('\n------area------\n')
    #     #     print(area.text.strip("\n"))
    #     #     print('\n-------area------END\n')
    #     o["title"]=allProperties[i].find("a",{"class":"item-link"}).text.strip("\n") #+ allProperties[i].find("div",{"class":"item-description"}).text.strip("\n")
    #     o["property-link"]="https://www.pisocompartido.com"+allProperties[i].find("a",{"class":"item-link"}).get('href')
    #     l.append(o)
    #     o={}



    # print("\n-------- вернул сайт -----------\n")
    # print(l)
    # print("\n-------- вернул сайт -----------конец\n")

    return l

def file_writer_pisocompartido(data):
# Записываем строки в новый CSV файл
    fieldnames = data[0].keys()
    with open('pisocompartido.csv', 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)

def file_writer_new_pisocompartido(data):
    # print("\n-------- data -----------\n")
    # print(data)
    # print("\n-------- data -----------конец\n")

#    now = datetime.datetime.now()
#    with open(domain+'_'+now.strftime("%Y-%m-%d_%H%M")+'.csv', 'w') as file:
    with open('pisocompartido_new.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('price','area-size','title','property-link'))
        for item in data:
            # print("\n-------- item in data -----------\n")
            # print(item)
            # print("\n-------- item in data -----------конец\n")
            a_pen.writerow((item))

def file_writer_for_error_pisocompartido(data):
#    now = datetime.datetime.now()
#    with open(domain+'_'+now.strftime("%Y-%m-%d_%H%M")+'.csv', 'w') as file:
    with open('pisocompartido.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('price','area-size','title','property-link'))
        for item in data:
            # print("\n-------- item in data for error -----------\n")
            # print(item)
            # print("\n-------- item in data -----------конец\n")
            a_pen.writerow((item['price'],item['area-size'],item['title'],item['property-link']))
    # exit()

def file_reader_pisocompartido():
    data = []
    with open('pisocompartido.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def file_reader_new_pisocompartido():
    data = []
    with open('pisocompartido_new.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def new_tasks_t_message_pisocompartido(mesage_rows):
    
    global bot
    global chat_id
    text_m=''
    iskluchit=[
        'еpепeчатать рyкoписный тeкcт'
               ]
    razreshen=1
    for row in mesage_rows:
        for int in iskluchit:
            if int in row['title']:
                razreshen=0
                print(' -X-', end=" ")    
        if razreshen>0:     #'price','area-size','title','property-link'
            text_m=text_m+str(row['price'])+'\n'+str(row['area-size'])+'\n'+str(row['title'])+'\n'+str(row['property-link'])+'\n'+'\n'
    # print('text_m\n')
    # print('text_m\n')
    # print('text_m\n')
    # print(text_m)
    # print('text_m_END\n')
    
    # Разбиваем длинное сообщение на более короткие
    max_length = 4000  # Максимальная длина одного сообщения
    chunks = [text_m[i:i+max_length] for i in range(0, len(text_m), max_length)]

    # Отправляем части сообщения последовательно
    #chat_id = 'USER_CHAT_ID'  # Замени на реальный идентификатор чата
    # exit()

    for chunk in chunks:
        bot.send_message(chat_id, chunk)




    # bot.send_message(chat_id, text=text_m)

def start_pisocompartido():
    firstStartAll=0
    global status

    global token  # токен телеграм бота
    global bot
    global chat_id  # Например chat_id = '223344'   

    # while True:
    try:

        # bot.send_message(chat_id, 'TEST')
        # exit()
        print('pisocompartido:   Вост+', end="|") 
        old_posts = file_reader_pisocompartido()
        # print('old_posts\n')
        # print('old_posts\n')
        # print('old_posts\n')
        # print(old_posts)
        # print('old_posts_END\n')
        print('Загр+', end="|") 
        all_posts = take_all_posts_pisocompartido()
        # print("\n-------- получил вернул сайт -----------\n")
        # print(all_posts)
        # print("\n-------- получил вернул сайт -----------конец\n")
        print('Новые+', end="|") 
        file_writer_new_pisocompartido(all_posts)
        # print('считано')
        all_posts = file_reader_new_pisocompartido() # Читаем из файла, для конвертации данных в нужный формат
        # print('all_posts\n')
        # print('all_posts\n')
        # print('all_posts\n')
        # print(all_posts)
        # print('all_posts_END\n')
        print('Новые+', end="|") 
        unique_rows = [row for row in all_posts if row not in old_posts]
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print(unique_rows)
        # print('unique_rows_END\n')
        print('Собщение+', end="|") 

        new_tasks_t_message_pisocompartido(unique_rows)
    
        all_posts = old_posts + unique_rows
        print('Сохр+', end="|")
        file_writer_pisocompartido(all_posts)
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('ВсеОК ', formatted_time)
        # exit()
        # time.sleep(3*60)
    except FileNotFoundError as e:
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print("Произошла ошибка:", e,' Исправляем.', formatted_time)
        all_posts = take_all_posts_pisocompartido()
        file_writer_for_error_pisocompartido(all_posts)

        #----------------- try --------------------------------
        # bot.send_message(chat_id, 'TEST')
        # exit()
        print('pisocompartido:   Вост+', end="|") 
        old_posts = file_reader_pisocompartido()
        # print('old_posts\n')
        # print('old_posts\n')
        # print('old_posts\n')
        # print(old_posts)
        # print('old_posts_END\n')
        print('Загр+', end="|") 
        all_posts = take_all_posts_pisocompartido()
        # print("\n-------- получил вернул сайт -----------\n")
        # print(all_posts)
        # print("\n-------- получил вернул сайт -----------конец\n")
        print('Новые+', end="|") 
        file_writer_new_pisocompartido(all_posts)
        all_posts = file_reader_new_pisocompartido() # Читаем из файла, для конвертации данных в нужный формат
        # print('all_posts\n')
        # print('all_posts\n')
        # print('all_posts\n')
        # print(all_posts)
        # print('all_posts_END\n')
        print('Новые+', end="|") 
        unique_rows = [row for row in all_posts if row not in old_posts]
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print('unique_rows\n')
        # print(unique_rows)
        # print('unique_rows_END\n')
        print('Собщение+', end="|") 

        new_tasks_t_message_pisocompartido(unique_rows)
    
        all_posts = old_posts + unique_rows
        print('Сохр+', end="|")
        file_writer_pisocompartido(all_posts)
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('ВсеОК ', formatted_time)
        # exit()
        # time.sleep(3*60)
        #------------------------try end-----------------------------------
    except Exception as e:
        # Обработка других исключений
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        print('\n','-'*50,'\n\n',traceback.format_exc(),'\n\n','='*50,'\n')  # Выведет всю трассировку ошибки
        print("Произошла ошибка:", e,' Рестарт через 3 мин.(',status,')   ', formatted_time)
        s_mes="pisocompartido:"+ str(e)+'|Р:3м('+str(status)+')'+ str(formatted_time)
        print(s_mes)
        bot.send_message(chat_id, s_mes)

        # exit()
        time.sleep(5)




# ===========================================================================


# Начальное время ожидания
start_time = time.time()
status=1

token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)
chat_id = os.getenv('TELEGRAM_CHAT_ID')


ts = 3*60 # Время ожидания между полными циклами програмы
pts = 3 # Сколько промежутков ожидания в программе (подпрограмм)
ts_use = ts/pts
ts_print=ts_use/60

while True:
    try:
        # print("\nok")
        # exit()
        # pts=4/0
        start_pisocompartido()
        # exit()
        time.sleep(ts_use)
        start_fotocasa()
        time.sleep(ts_use)
        start_idealista()
        time.sleep(ts_use)
        # start_badi()
        # time.sleep(ts_use)
    except Exception as e:
        # Обработка других исключений
        # Получаем текущее время
        current_time = datetime.now()
        # Форматируем и выводим время
        time_format = "%H:%M"
        formatted_time = current_time.strftime(time_format)
        ts_print=ts/60
        print('\n','-'*50,'\n\n',traceback.format_exc(),'\n\n','='*50,'\n')  # Выведет всю трассировку ошибки
        print("\n\nПроизошла глобальная ошибка:", e,' Рестарт через ', ts_print, ' мин.(',status,')   ', formatted_time, '\n\n')
        s_mes="Глобальная ошибка:  "+ str(traceback.format_exc())+'  |Р:3м('+str(status)+')'+ str(formatted_time)
        print(s_mes)
        try:
            bot.send_message(chat_id, s_mes)
        except Exception as e:
            print('\n','-'*50,'\n\n',traceback.format_exc(),'\n\n','='*50,'\n')  # Выведет всю трассировку ошибки
            print("\n\nПроизошла глобальная ошибка в bot.send_message(chat_id, s_mes):", e,' Рестарт через ', ts_print, ' мин.(',status,')   ', formatted_time, '\n\n')
        # exit()
        time.sleep(ts)

