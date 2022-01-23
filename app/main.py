import time

from app.src.ripio.RipioRequestService import RipioRequestService
from src.ripio.RipioRequestApi import RipioRequestApi
from src.infrastructure.repository.Repository import Repository


def main():
    ripio = RipioRequestApi()
    repo = Repository()
    while True:

        ripio.getDataFromApi(endpoint="rate/USDC_ARS",table= "rate")
        ripio.getDataFromApi(endpoint="rate/BTC_USDC", table="rate")
        ripio.getDataFromApi(endpoint="rate/BTC_ARS", table="rate")
        time.sleep(int(repo.getConfig("request_time")))


if __name__ == '__main__':
    print("Ripio Api App")
    main()
