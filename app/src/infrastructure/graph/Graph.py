import matplotlib.pyplot as plt
import numpy as np

from app.src.infrastructure.rate.RateQueries import AVERAGE_RATE, ALL_RATES_PAIR
from app.src.infrastructure.repository.Repository import Repository


class Graph:
    def __init__(self):
        self.plt = plt
        self.np = None

    def makeGraph(self,data):
        # create data
        values = np.ptp(data)
        # use the plot function
        self.plt.plot(values)

    def showGraph(self, block=False):
        self.plt.show(block=block)

import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above)


#
#
# g = Graph()
# data = []
# i = 0
# repository = Repository()
# result = repository.retrieveData(ALL_RATES_PAIR, ["USDC_ARS"])
# for x in result:
#     print(x[1])
#     data.append(x[1])
#     i+=30
# # g.makeGraph(data)
# # g.showGraph(block=True)
#
# df = sns.load_dataset('penguins')
# sns.set(style="darkgrid")
#
# sns.histplot(data=df, x="sex", color="skyblue", label="Sepal Length", kde=True)
# # sns.histplot(data=df, x="sepal_width", color="red", label="Sepal Width", kde=True)
#
# plt.legend()
# plt.show()
