import datetime
import os
import sys
import time

import numpy as np
import tushare as ts


def download_tick_data_to_file(shares=None, start=None, end=None):
    stockBasics = ts.get_stock_basics()

    if not shares:
        shares = stockBasics.index.tolist()
    for share in shares:
        print("process {}:".format(share))

        dataDirectory = os.path.expanduser("~") + "/project/data/" + share + "/"
        try:
            os.mkdir(dataDirectory)
            print("mkdir {}".format(dataDirectory))
        except FileExistsError:
            pass

        today = datetime.datetime.today()
        if end is None:
            endDay = today
            if str(today.time()) < '15:01:00':
                endDay -= datetime.timedelta(days = 1)
        else:
            endDay = datetime.datetime.strptime(end, "%Y-%m-%d")
        if start is None:
            startDay = datetime.datetime(year = endDay.year - 1, month = endDay.month, day = endDay.day)
        else:
            startDay = datetime.datetime.strptime(start, "%Y-%m-%d")
        timeToMarket = datetime.datetime.strptime(str(stockBasics.ix[share].timeToMarket), "%Y%m%d")
        if startDay < timeToMarket:
            startDay = timeToMarket

        tradingDays = ts.get_hist_data('sh', startDay.date().isoformat(), endDay.date().isoformat()).index.tolist()
        day = startDay
        while day <= endDay:
            if day.date().isoformat() in tradingDays:
                print("check {}".format(str(day.date())))
                dataFile = dataDirectory + day.date().isoformat() + ".csv"
                if not os.path.exists(dataFile):
                    print("getting data")
                    try:
                        df = ts.get_tick_data(share, date = day.date().isoformat())
                        print("write file {}".format(dataFile))
                        df.to_csv(dataFile)
                    except IOError:
                        # wait 10 minutes
                        time.sleep(300)
                        continue
            day += datetime.timedelta(days = 1)


if __name__ == '__main__':
    download_tick_data_to_file(sys.argv[1:])
