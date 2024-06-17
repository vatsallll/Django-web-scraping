from celery import shared_task
from .coinmarketcap import CoinMarketCap

@shared_task
def scrape_coin_data(coin_acronyms):
    scraper = CoinMarketCap()
    results = []
    for coin in coin_acronyms:
        data = scraper.get_coin_data(coin)
        results.append({"coin": coin, "output": data})
    scraper.close()
    return results
