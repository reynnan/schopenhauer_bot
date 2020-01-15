from requests import get
from lxml import html
from random import randint

def get_quotes(url, xpath):
    response = get(url)
    doc = html.fromstring(response.content)
    raw_quotes = doc.xpath(xpath)
    return [quote.strip() for quote in raw_quotes]


def get_random_quote(url, xpath):
    quotes = get_quotes(url, xpath)
    random_quote_index = randint(0, len(quotes) - 1)
    return quotes[random_quote_index]

