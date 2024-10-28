import re
import Tokenizer as Token
from urllib.parse import urlparse, urlunparse, parse_qs
from bs4 import BeautifulSoup
from simhash import Simhash

if __name__ == "__main__":
    print(parse_qs(urlparse("https://ics.uci.edu/happening/news/?filter%5Bunits%5D=69&filter%5Baffiliation_posts%5D=1990&filter%5Bpartnerships_posts%5D=2002&filter%5Bresearch_areas_ics%5D=1994").query))