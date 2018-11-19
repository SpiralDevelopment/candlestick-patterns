from candlestick.patterns.candlestick_finder import CandlestickFinder


class RainDropDoji(CandlestickFinder):
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 2, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]
        prev_candle = self.data.iloc[idx + 1 * self.multi_coeff]

        close = candle[self.close_column]
        open = candle[self.open_column]
        high = candle[self.high_column]
        low = candle[self.low_column]

        prev_close = prev_candle[self.close_column]
        prev_open = prev_candle[self.open_column]
        prev_high = prev_candle[self.high_column]
        prev_low = prev_candle[self.low_column]

        return (prev_close < prev_open and
                abs(prev_close - prev_open) / (prev_high - prev_low) >= 0.7 and
                abs(close - open) / (high - low) < 0.1 and
                prev_close > close and
                prev_close > open and
                (high - max(close, open)) > (3 * abs(close - open)) and
                (min(close, open) - low) > (3 * abs(close - open)))
