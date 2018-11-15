import pandas as pd
from pandas.api.types import is_numeric_dtype


class CandlestickFinder(object):

    def __init__(self, name, required_count):
        self.name = name
        self.required_count = required_count
        self.close_column = 'close'
        self.open_column = 'open'
        self.low_column = 'low'
        self.high_column = 'high'
        self.data = None

    def has_pattern(self,
                    candles_df,
                    ohlc,
                    is_reversed):
        self.prepare_data(candles_df,
                          ohlc,
                          is_reversed)

    def prepare_data(self, candles_df, ohlc, is_reversed):

        if isinstance(candles_df, pd.DataFrame):

            if len(candles_df) >= self.required_count:
                if ohlc and len(ohlc) == 4:
                    if not set(ohlc).issubset(candles_df.columns):
                        raise Exception('Provided columns does not exist in given data frame')

                    self.open_column = ohlc[0]
                    self.high_column = ohlc[1]
                    self.low_column = ohlc[2]
                    self.close_column = ohlc[3]
                else:
                    raise Exception('Provide list of four elements indicating columns in strings. '
                                    'Default: open, high, low, close')

                if not is_numeric_dtype(candles_df[self.close_column]):
                    candles_df[self.close_column] = pd.to_numeric(candles_df[self.close_column])

                if not is_numeric_dtype(candles_df[self.open_column]):
                    candles_df[self.open_column] = pd.to_numeric(candles_df[self.open_column])

                if not is_numeric_dtype(candles_df[self.low_column]):
                    candles_df[self.low_column] = pd.to_numeric(candles_df[self.low_column])

                if not is_numeric_dtype(candles_df[self.high_column]):
                    candles_df[self.high_column] = pd.to_numeric(candles_df[self.high_column])

                if not is_reversed:
                    self.data = candles_df.iloc[::-1]
                else:
                    self.data = candles_df
            else:
                raise Exception('{0} requires at least {1} data'.format(self.name,
                                                                        self.required_count))
        else:
            raise Exception('Candles must be in Panda data frame type')
