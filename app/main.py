import time

from src.ripio.RipioRequestApi import RipioRequestApi
from src.infrastructure.repository.Repository import Repository

ripio = RipioRequestApi()
repo = Repository()

def main():

    while True:

        ripio.getDataFromApi(endpoint="rate/USDC_ARS",table= "rate")
        ripio.getDataFromApi(endpoint="rate/BTC_USDC", table="rate")
        ripio.getDataFromApi(endpoint="rate/BTC_ARS", table="rate")

        # RateService().getAverageRateForPair()
        #time.sleep(int(repo.getConfig("request_time")))
        time.sleep(60)

if __name__ == '__main__':
    print("Ripio Api App")
    main()
