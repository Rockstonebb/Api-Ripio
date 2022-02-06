from ..rate.RateQueries import AVERAGE_RATE, ALL_RATES_PAIR
from ..repository.Repository import Repository


class RateService:
    def __init__(self):
        self.repo = Repository()
        self.data = None

    def getAverageRateForPair(self, pair="BTC_USDC"):
        data = self.repo.retrieveData(query=AVERAGE_RATE, param=[pair])
        if(data is not None):
            for x in data:
                print(x)

    def getAllValuesForPair(self, pair="BTC_USDC"):
        data = self.repo.retrieveData(query=ALL_RATES_PAIR, param=[pair])
        if (data is not None):
            for x in data:
                print(x)
