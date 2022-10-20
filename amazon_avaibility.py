import now
import urllib3
from bs4 import BeautifulSoup
from datetime import datetime


AVAILABLE = 'Disponibile.'
NOT_AVAILABLE = 'Non disponibile.'


# ====================
# MacBook Air M2 -> Disponibile.
item_url = 'https://amzn.to/3TwjJGP'
# ====================

http = urllib3.PoolManager()
response = http.request('GET', item_url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.data, 'html.parser')
# print(soup.prettify())


# cerco il tag con id 'availability'
availability_check = soup.find('div', {'id': 'availability'})


# stampo la data e l'ora
current_datetime = datetime.now()
dt_string = current_datetime.strftime("%d/%m/%Y - %H:%M:%S")
print('[', dt_string, ']', end=' ')


# se trovo il tag con id 'availability' ..
if availability_check:

    # .. prendo il testo contenuto al suo interno
    is_available_string = availability_check.findChild('span').string.strip()

    # .. se il testo non contiene 'Non disponibile' ..
    if is_available_string != NOT_AVAILABLE:

        # .. allora stampo 'Disponibile'
        print(AVAILABLE)

    # .. altrimenti ..
    else:

        # .. stampo 'Non disponibile.'
        print(NOT_AVAILABLE)

# .. altrimenti ..
else:

    # .. stampo 'Non disponibile.'
    print(NOT_AVAILABLE)