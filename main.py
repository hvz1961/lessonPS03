from bs4 import BeautifulSoup
import requests
from googletrans import Translator

#Создадим мини-игру
#Создаём функцию, которая будет получать информацию

def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()

        return {
            'english_words': english_words,
            'word_definition': word_definition
        }
    except:
        print('Произошда ошибка')
        return None
def translate_word(word):
    translator = Translator()
    translation_word = translator.translate(word, src='en', dest='ru')
    return translation_word.text
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
            translation = translate_word(word)
            print(f'Перевод слова "{word}": {translation}')
        else:
            print(f'Ответ неверный, было слово - {word}')
            translation = translate_word(word)
            print(f'Перевод слова "{word}": {translation}')

        play_again = input('Хотите сыграть еще раз? y/n')
        if play_again != 'y':
            print('Спасибо за игру!')
            break

word_game()
            
    
# translator = Translator()
# result = translator.translate('dog', 'ru')
# print(result.text)

        








