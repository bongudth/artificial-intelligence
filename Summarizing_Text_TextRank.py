import warnings
warnings.filterwarnings("ignore")

print('\n')

# Import BeautifulSoup and urllib libraries to fetch data from Wikipedia.
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Function to get data from Wikipedia
def get_only_text(url):
    # Fetch the data from Wikipedia
    page = urlopen(url)
    # Parse the data using BeautifulSoup
    soup = BeautifulSoup(page)
    # Get the text from the data
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))

    return text

# Mention the Wikipedia url
url = 'https://en.wikipedia.org/wiki/Natural_language_processing'

# Call the function created above
text = get_only_text(url)

# Import summarize from gensim
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

# Convert text to string format
text = str(text)

#Summarize the text with ratio 0.1 (10% of the total words.)
summary = summarize(text, ratio=0.1)
print('Summary:\n\n', summary, end='\n\n')

# keywords
keywords = keywords(text, ratio=0.1)
print('Keywords:\n\n', keywords)