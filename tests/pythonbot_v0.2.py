from oanda_bot import Bot

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
    # trading environment (default=practice)
    environment='practice',
    # trading currency (default=EUR_USD)
    instrument='USD_JPY',
    # 1 minute candlesticks (default=D)
    granularity='M5',
    # trading time (default=Bot.SUMMER_TIME)
    trading_time=Bot.SUMMER_TIME,
    # Slack notification when an error occurs
    # slack_webhook_url='<your slack webhook url>',
    # Line notification when an error occurs
    # line_notify_token='<your line notify token>',
    # Discord notification when an error occurs
    # discord_webhook_url='<your discord webhook url>',
).run()