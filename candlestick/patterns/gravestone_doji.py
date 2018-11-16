from candlestick.patterns.candlestick_finder import CandlestickFinder


class GravestoneDoji(CandlestickFinder):
    def __init__(self, target=None):
        super().__init__(self.get_class_name(), 1, target=target)

    def logic(self, idx):
        candle = self.data.iloc[idx]

        close = candle[self.close_column]
        open = candle[self.open_column]
        high = candle[self.high_column]
        low = candle[self.low_column]

        return (abs(close - open) / (high - low) < 0.1 and
                (high - max(close, open)) > (3 * abs(close - open)) and
                (min(close, open) - low) <= abs(close - open))
