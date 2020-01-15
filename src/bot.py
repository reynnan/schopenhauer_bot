from random import randint
from quote import get_random_quote
from twitter import TWITTER_API, tweet_new_quote

# GOOD READS CONFIG
GOOD_READS_URL = "https://www.goodreads.com/author/quotes/11682.Arthur_Schopenhauer?page=" + str(randint(1, 5))
GOOD_READS_QUOTE_XPATH = './/div[@class="quoteText"]/br[1]/preceding-sibling::text()[1]'


schopenhauers_quote = get_random_quote(GOOD_READS_URL, GOOD_READS_QUOTE_XPATH)
tweeted_quote_object = tweet_new_quote(TWITTER_API.update_status, schopenhauers_quote)
print(tweeted_quote_object.text)


