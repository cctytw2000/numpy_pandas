import pandas as pd
import numpy as np
series1 = pd.Series(np.random.randint(0, 101, 50))


def check(series):
    if series < 60:
        return'待加強'
    elif series < 80:
        return '佳'
    else:
        return'優良'


def printgroup(seriesgroup):
    for k, v in seriesgroup:
        print(k)
        print(v)
        print("="*50)


by_series = series1.apply(check)
series1_group = series1.groupby(by_series)
print(printgroup(series1_group))
print(series1_group.count())
