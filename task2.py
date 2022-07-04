import json
from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

final_dict = {}


def main(link: str):
    while True:
        r = requests.get(link, headers=headers)
        if r.status_code == 404:
            break
        bs = BeautifulSoup(r.text, "lxml")
        all_animals = bs.find(class_="mw-content-ltr").find(class_="mw-category mw-category-columns").find(
            class_="mw-category-group").find("ul")
        for animal in all_animals:
            animal_name = animal.text.replace("\n", "")
            if animal_name:
                try:
                    final_dict[animal_name[0]] += 1
                except KeyError as e:
                    final_dict[animal_name[0]] = 1
            continue
        next_page = bs.find(class_="mw-category-generated").find(id="mw-pages").find_all("a")
        link = "https://ru.wikipedia.org/" + next_page[-1].get("href")
        link_text = next_page[-1].text
        if link_text == "Предыдущая страница":
            break
    with open("final_dict.json", "w") as file:
        json.dump(final_dict, file, indent=4, ensure_ascii=False)
    return print(final_dict)


main("https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F%3A%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from=%D0%90")
