from candlestick_patterns.candlestick_finder import CandlestickFinder


class DragonflyDoji(CandlestickFinder):
    def __init__(self):
        super().__init__('DragonFly Doji', 1)

    def has_pattern(self,
                    candles_df,
                    ohlc,
                    is_reversed):
        super().has_pattern(candles_df,
                            ohlc,
                            is_reversed)

        last_candle = self.data.iloc[0]

        close = last_candle[self.close_column]
        open = last_candle[self.open_column]
        high = last_candle[self.high_column]
        low = last_candle[self.low_column]

        return abs(close - open) / (high - low) < 0.1 and \
               (min(close, open) - low) > (3 * abs(close - open)) and \
               (high - max(close, open)) < abs(close - open)
