import candlestick
import pandas as pd
import requests


candles = requests.get('https://api.binance.com/api/v1/klines?symbol=ADABTC&interval=4h')
candles_dict = candles.json()

columns = ['T', 'open', 'high', 'low', 'close', 'V', 'CT', 'QV', 'N', 'TB', 'TQ', 'I']

candles_df = pd.DataFrame(candles_dict, columns=columns)

candles_df = candlestick.doji_star(candles_df)
candles_df = candlestick.bearish_harami(candles_df)
candles_df = candlestick.bullish_harami(candles_df)
candles_df = candlestick.dark_cloud_cover(candles_df)
candles_df = candlestick.doji(candles_df)
candles_df = candlestick.dragonfly_doji(candles_df)
candles_df = candlestick.hanging_man(candles_df)

print(candles_df)
