import requests
import selectorlib
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

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
    date = now.strftime("%d-%m-%Y %H:%M:%S")
    with open("data.txt", "a") as file:
        line = f"{date},{extracted}\n"
        return file.write(line)



if __name__ == "__main__":
    scraped =  scraping(URL)
    extracted = extract(scraped)
    stored = store(extracted)







