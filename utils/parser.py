from bs4 import BeautifulSoup

def parser(html_text):

    soup = BeautifulSoup(html_text , "html.parser")

    results = soup.select("article.result")
    result_list_items = soup.select("li.js-db-result-item")

    print(f"Articles found : {len(results)}")
    print(f"Result list items found : {len(result_list_items)}")

    print("\n")

    for index , result_item in enumerate(result_list_items , start = 1):

        articles = result_item.select("article.result")
        print(f"List item {index} : "
              f"Articles found : {len(articles)} article (s)")