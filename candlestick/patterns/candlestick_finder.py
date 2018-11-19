import pandas as pd
from pandas.api.types import is_numeric_dtype


class CandlestickFinder(object):
    def __init__(self, name, required_count, target=None):
        self.name = name
        self.required_count = required_count
        self.close_column = 'close'
        self.open_column = 'open'
        self.low_column = 'low'
        self.high_column = 'high'
        self.data = None
        self.is_data_prepared = False
        self.multi_coeff = -1

        if target:
            self.target = target
        else:
            self.target = self.name

    def get_class_name(self):
        return self.__class__.__name__

    def logic(self, row_idx):
        raise Exception('Implement the logic of ' + self.get_class_name())

    def has_pattern(self,
                    candles_df,
                    ohlc,
                    is_reversed):
        self.prepare_data(candles_df,
                          ohlc)

        if self.is_data_prepared:
            results = []
            rows_len = len(candles_df)
            idxs = candles_df.index.values

            if is_reversed:
                self.multi_coeff = 1

                for row_idx in range(rows_len - 1, -1, -1):

                    if row_idx <= rows_len - self.required_count:
                        results.append([idxs[row_idx], self.logic(row_idx)])
                    else:
                        results.append([idxs[row_idx], None])

            else:
                self.multi_coeff = -1

                for row in range(0, rows_len, 1):

                    if row >= self.required_count - 1:
                        results.append([idxs[row], self.logic(row)])
                    else:
                        results.append([idxs[row], None])

            candles_df = candles_df.join(pd.DataFrame(results, columns=['row', self.target]).set_index('row'),
                                         how='outer')

            return candles_df
        else:
            raise Exception('Data is not prepared to detect patterns')

    def prepare_data(self, candles_df, ohlc):

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
                                    'Default: [open, high, low, close]')

                self.data = candles_df.copy()

                if not is_numeric_dtype(self.data[self.close_column]):
                    self.data[self.close_column] = pd.to_numeric(self.data[self.close_column])

                if not is_numeric_dtype(self.data[self.open_column]):
                    self.data[self.open_column] = pd.to_numeric(self.data[self.open_column])

                if not is_numeric_dtype(self.data[self.low_column]):
                    self.data[self.low_column] = pd.to_numeric(self.data[self.low_column])

                if not is_numeric_dtype(self.data[self.high_column]):
                    self.data[self.high_column] = pd.to_numeric(candles_df[self.high_column])

                self.is_data_prepared = True
            else:
                raise Exception('{0} requires at least {1} data'.format(self.name,
                                                                        self.required_count))
        else:
            raise Exception('Candles must be in Panda data frame type')
