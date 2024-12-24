import requests
import json
import webbrowser
import urllib.parse

class WikipediaSearch:
    def __init__(self):
        self.base_url = "https://ru.wikipedia.org/w/api.php"

    def search_articles(self, query):
        # URL-кодирование запроса
        encoded_query = urllib.parse.quote(query)
        # Формирование URL для запроса к API Википедии
        url = f"{self.base_url}?action=query&list=search&utf8=&format=json&srsearch={encoded_query}"

        # Выполнение запроса
        response = requests.get(url)
        data = response.json()

        # Получение результатов поиска
        return data['query']['search']

    def display_search_result(self, results):
        print("Результаты поиска:")
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result['title']}")

    def open_article_page(self, pageid):
        url = f"https://ru.wikipedia.org/w/index.php?curid={pageid}"
        webbrowser.open(url)

if __name__ == "__main__":
    app = WikipediaSearch()
    query = input("Введите поисковый запрос: ")
    results = app.search_articles(query)

    if not results:
        print("Ничего не найдено.")
    else:
        app.display_search_result(results)

        try:
            choice = int(input("Введите номер статьи для открытия: "))
            if 1 <= choice <= len(results):
                selected_result = results[choice - 1]
                app.open_article_page(selected_result['pageid'])
            else:
                print("Неверный выбор.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")
