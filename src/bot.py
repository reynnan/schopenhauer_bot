from random import randint
from quote import get_random_quote
from twitter import TWITTER_API, tweet_new_quote

HASHTAGS = ["#Schopenhauer", "#philosophy", "#quote"]
# GOOD READS CONFIG
GOOD_READS_URL = "https://www.goodreads.com/author/quotes/11682.Arthur_Schopenhauer?page=" + str(randint(1, 5))
GOOD_READS_QUOTE_XPATH = './/div[@class="quoteText"]/br[1]/preceding-sibling::text()[1]'


quote = get_random_quote(GOOD_READS_URL, GOOD_READS_QUOTE_XPATH)
quote_with_hashtags = f"{quote} {' '.join(HASHTAGS)}"
tweeted_quote_object = tweet_new_quote(TWITTER_API.update_status, quote_with_hashtags)
print(tweeted_quote_object.text)


