import requests
import json
import webbrowser
import urllib.parse

def search_wikipedia(query):
    # URL-кодирование запроса
    encoded_query = urllib.parse.quote(query)
    # Формирование URL для запроса к API Википедии
    url = f"https://ru.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json&srsearch={encoded_query}"

    # Выполнение запроса
    response = requests.get(url)
    data = response.json()

    # Получение результатов поиска
    search_results = data['query']['search']
    return search_results

def display_search_results(results):
    print("Результаты поиска:")
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result['title']}")

def open_wikipedia_page(pageid):
    url = f"https://ru.wikipedia.org/w/index.php?curid={pageid}"
    webbrowser.open(url)

def main():
    query = input("Введите поисковый запрос: ")
    results = search_wikipedia(query)

    if not results:
        print("Ничего не найдено.")
        return

    display_search_results(results)

    try:
        choice = int(input("Введите номер статьи для открытия: "))
        if 1 <= choice <= len(results):
            selected_result = results[choice - 1]
            open_wikipedia_page(selected_result['pageid'])
        else:
            print("Неверный выбор.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")

if __name__ == "__main__":
    main()
