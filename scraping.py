import csv
import requests
from bs4 import BeautifulSoup


def scraping()

    url = ""

    filename = "scraping.csv"
    f = open(filename, "w", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    title = "".split(",")
    writer.writerow(title)


    pages = ["?a", "?b", "?c"]

    for page in pages:
        res = requests.get(url + page)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        data_rows = soup.find("table", attrs={"id":"id_name"}).find("tbody").find_all("tr")
        for row in data_rows:
            columns = row.find_all("td")
            data = [column.get_text().strip() for column in columns]
            writer.writerow(data)
        
        writer.writerow(" ")


if __name__ == "__main__":
    scraping()
