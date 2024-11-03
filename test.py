import re
import shelve
import Tokenizer as Token
from urllib.parse import urlparse, urlunparse, parse_qs
from bs4 import BeautifulSoup
from simhash import Simhash

if __name__ == "__main__":
    result = 0
    with shelve.open("report") as report:
        for key in report:
            print(f"{key}: {report[key]}")
            if "." in key:
                result += report[key]
    print(result)

    with shelve.open("report2") as db:
        data = dict(db)
        top_50 = sorted(data.items(), key=lambda item: item[1], reverse=True)[:50]
    for key, value in top_50:
        print(f"{key}: {value}")
