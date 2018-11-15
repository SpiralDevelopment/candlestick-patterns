import candlestick
import pandas as pd
import requests


candles = requests.get('https://api.binance.com/api/v1/klines?symbol=ADABTC&interval=1h')
candles_dict = candles.json()

columns = ['T', 'open', 'high', 'low', 'close', 'V', 'CT', 'QV', 'N', 'TB', 'TQ', 'I']

candles_df = pd.DataFrame(candles_dict, columns=columns)

res = candlestick.bullish_harami(candles_df)
print(res)

res = candlestick.bearish_harami(candles_df)
print(res)

res = candlestick.dark_cloud_cover(candles_df)
print(res)

res = candlestick.doji(candles_df)
print(res)

res = candlestick.dragonfly_doji(candles_df)
print(res)
