from bs4 import BeautifulSoup
import requests
from googletrans import Translator

# url = 'http://quotes.toscrape.com/'

# response = requests.get(url)
# print(response.content) # можно указать .text или .content
# создаем переменную куда будем сохранять данные
# html = response.text
# теперь создаем объект
# soup = BeautifulSoup(html, 'html.parser')
# создаем переменную для ссылок с нашего сайта
# link = soup.find_all('a')
# # print(link) # при такой команде будет выводится данные не удобно, поэтому поменяем команду
# for link in link:
#     print(link.get('href'))
# при таком формате вывода информации: с помощью атрибута 'href'
# мы увидим все ссылки, которые есть на сайте.

# Парсинг цитат
# url = 'http://quotes.toscrape.com/'
# response = requests.get(url)
# html = response.text

# soup = BeautifulSoup(html, 'html.parser')
#Создадим отдельную переменную text, куда будут сохраняться все цитаты
# text = soup.find_all('span', 'text')
# print(text)
#Создадим отдельную переменную author, куда будут сохраняться все авторы
# author = soup.find_all('small', 'author')
# print(author)
#при этом информация будет выводится в виде списка,
#чтобы инф. была наглядной применяем команду for
#С помощью функции range(len) определим общее количество цитат
# for i in range(len(text)):
#Присвоим номер каждой цитате так, чтобы нумерация шла с 1
#     print(f'Цитата номер - {i + 1}')
#Выводим саму цитату, указывая её id
#     print(text[i].text)
#Выводим автора цитаты
#     print(f'Автор цитаты - {author[i].text}\n') #указываем в конце \n
# для отступа между цитатами

#Создадим мини-игру
#Создаём функцию, которая будет получать информацию

translator = Translator()
result = translator.translate('dog', 'ru')
print(result.text)
def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
       
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', 'id=rundom_word_definition').text.strip()

        return {
            'english_words': english_words,
            'word_definition': word_definition
        }
    except:
        print('Произошда ошибка')

def word_game():
    print('Добро пожаловать в игру')
    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        print(f'Значение слова - {word_definition}')
        user = input('Что это за слово?')
        if user == word:
            print('Все правильно')
        else:
            print(f'Ответ неверный, было слово - {word}')

        play_again = input('Хотите сыграть еще раз? y/n')
        if play_again != 'y':
            print('Спасибо за игру!')
            break

word_game()
            
    


        








