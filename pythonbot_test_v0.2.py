from oanda_bot import Bot
# https://medium.com/geekculture/combining-the-ultimate-oscillator-with-the-stochastic-oscillator-in-a-trading-strategy-a917137d1705
class MyBot(Bot):
    def strategy(self):
        stoch = self.stoch(k_period=14)
        ao = self.ao()
        self.buy_entry = (stoch[0] <= 25) & (ao<35)
        self.buy_exit = (stoch[0] >= 75)
        self.sell_entry = (stoch[0] >= 75) & (ao>65)
        self.sell_exit = (stoch[0] <= 25)
        
        self.units = 1000 # currency unit (default=10000)
        self.take_profit = 100 # take profit pips (default=0 take profit none)
        self.stop_loss = 20 # stop loss pips (default=0 stop loss none)

MyBot(
    account_id='101-004-9738850-003',
    access_token='b14e066294462edcf1c61f4caab62173-edf4ee118acf544baf3e1865d9ce33d3',
    instrument='USD_JPY',
    granularity='M5', # 15 second candlestick
).backtest(from_date="2021-9-1", to_date="2021-10-10", filename="backtest.png")