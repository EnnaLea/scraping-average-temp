import requests
import selectorlib
from datetime import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data_temperature.db")

now = datetime.now()

def scraping(url):
    response = requests.get(url, HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value

def store(extracted):
    date = now.strftime("%d-%m-%Y %H:%M:%S").strip()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES(?, ?)", (date, extracted))
    connection.commit()





if __name__ == "__main__":
    scraped =  scraping(URL)
    extracted = extract(scraped)
    stored = store(extracted)







