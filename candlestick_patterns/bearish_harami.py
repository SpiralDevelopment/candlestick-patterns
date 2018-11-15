from candlestick_patterns.candlestick_finder import CandlestickFinder


class BearishHarami(CandlestickFinder):

    def __init__(self):
        super().__init__('Bearish Harami', 2)

    def has_pattern(self,
                    candles_df,
                    ohlc,
                    is_reversed):
        super().has_pattern(candles_df,
                            ohlc,
                            is_reversed)

        last_candle = self.data.iloc[0]
        second_last_candle = self.data.iloc[1]

        close = last_candle[self.close_column]
        open = last_candle[self.open_column]
        high = last_candle[self.high_column]
        low = last_candle[self.low_column]

        second_close = second_last_candle[self.close_column]
        second_open = second_last_candle[self.open_column]
        second_high = second_last_candle[self.high_column]
        second_low = second_last_candle[self.low_column]

        return second_close > second_open and \
               abs(second_close - second_open) / (second_high - second_low) >= 0.7 and \
               0.3 > abs(close - open) / (high - low) >= 0.1 and \
               high < second_close and \
               low > second_open
