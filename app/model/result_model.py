from pydantic import BaseModel
from datetime import datetime


class ResultModel(BaseModel):
    min_average: int
    max_average: int
    final_value: float


class Base(object):
    def __init__(self, date, code):
        self.date = date
        self.code = code


# 证券信息
class Stock(object):
    def __init__(self, stockCode, name, ipoDate, outDate, type, status):
        self.stockCode = stockCode
        self.name = name
        self.ipoDate = str(ipoDate)
        self.outDate = str(outDate)
        self.type = type
        self.status = status


# class Stock(BaseModel):
#     stockCode: str
#     name: str
#     ipoDate: datetime
#     outDate: datetime
#     type: str
#     status: str


# 指数信息
class Index(Base):
    def __init__(self, date, code, open, high, low, close, preclose, volume,
                 amount, adjustflag, turn, tradestatus, pctchg):
        Base.__init__(self, date, code)
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.preclose = preclose
        self.volume = volume
        self.amount = amount
        self.adjustflag = adjustflag
        self.preclose = preclose
        self.turn = turn
        self.tradestatus = tradestatus
        self.pctchg = pctchg


class Hist(object):
    def __init__(self, date, code, close):
        self.date = str(date)
        self.code = code
        self.close = close
