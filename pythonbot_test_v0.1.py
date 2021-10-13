from oanda_bot import Bot

class MyBot(Bot):
    def strategy(self):
        rsi = self.rsi(period=10)
        ema = self.ema(period=20)
        lower = ema - (ema * 0.0001)
        upper = ema + (ema * 0.0001)
        self.buy_entry = (rsi < 30) & (self.df.C < lower)
        self.sell_entry = (rsi > 70) & (self.df.C > upper)
        self.sell_exit = ema > self.df.C
        self.buy_exit = ema < self.df.C
        self.units = 1000 # currency unit (default=10000)
        self.take_profit = 50 # take profit pips (default=0 take profit none)
        self.stop_loss = 20 # stop loss pips (default=0 stop loss none)

MyBot(
    account_id='101-004-9738850-003',
    access_token='b14e066294462edcf1c61f4caab62173-edf4ee118acf544baf3e1865d9ce33d3',
    instrument='USD_JPY',
    granularity='S15', # 15 second candlestick
).backtest(from_date="2021-7-7", to_date="2021-7-13", filename="backtest.png")