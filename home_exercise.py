import requests
from bs4 import BeautifulSoup
import googletrans

translator = googletrans.Translator()

def get_english_world():
    url = "https://randomword.com/"
    response = requests.get(url)
    #print(response.text)

    soup = BeautifulSoup(response.content, "html.parser")
    english_world = soup.find("div", id="random_word").text.strip()
    russian_word = translator.translate(english_world, dest="ru").text.strip()
    english_definition = soup.find("div", id="random_word_definition").text.strip()
    russian_definition = translator.translate(english_definition, dest="ru").text.strip()

    return {
        "english_world": english_world,
        "english_definition": english_definition,
        "russian_word": russian_word,
        "russian_definition": russian_definition
    }


def word_game():
    print("Добро пожаловать в игру")
    user_cnt = 0
    computer_cnt = 0

    while True:
        try:
            word_dict = get_english_world()
            english_world = word_dict["english_world"]
            english_definition = word_dict["english_definition"]
            russian_word = word_dict["russian_word"]
            russian_definition = word_dict["russian_definition"]

            print(f"Значение слова: {russian_definition}")
            print(f"English: {english_definition}")
            user_word = input("Введите слово: ")

            if user_word == english_world:
                print("True!")
                user_cnt += 1
            elif user_word == russian_word:
                print("Правильно!")
                user_cnt += 1
            else:
                print(f"Неверно, загадано слово: {russian_word} / {english_world}")
                computer_cnt += 1

        except:
            print("No words found")

        play_again = input("Хотите сыграть еще раз? y,д ")
        if play_again != 'y':
            print(f"Результат: {user_cnt}:{computer_cnt}")
            break

word_game()