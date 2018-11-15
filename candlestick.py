import re

__builders = dict()
__default_ohlc = ['open', 'high', 'low', 'close']


def __get_file_name(class_name):
    res = re.findall('[A-Z][^A-Z]*', class_name)
    return '_'.join([cur.lower() for cur in res])


def __load_module(module_path):
    p = module_path.rfind('.') + 1
    super_module = module_path[p:]
    try:
        module = __import__(module_path, fromlist=[super_module], level=0)
        return module
    except ImportError as e:
        raise e


def __get_class_by_name(class_name):
    file_name = __get_file_name(class_name)
    mod_name = 'candlestick_patterns.' + file_name

    if mod_name not in __builders:
        module = __load_module(mod_name)
        __builders[mod_name] = module
    else:
        module = __builders[mod_name]
    return getattr(module, class_name)


def __create_object(class_name):
    return __get_class_by_name(class_name)()


def bearish_harami(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False):
    bear_harami = __create_object('BearishHarami')
    return bear_harami.has_pattern(candles_df, ohlc, is_reversed)


def bullish_harami(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False):
    bull_harami = __create_object('BullishHarami')
    return bull_harami.has_pattern(candles_df, ohlc, is_reversed)


def dark_cloud_cover(candles_df,
                     ohlc=__default_ohlc,
                     is_reversed=False):
    dcc = __create_object('DarkCloudCover')
    return dcc.has_pattern(candles_df, ohlc, is_reversed)


def doji(candles_df,
         ohlc=__default_ohlc,
         is_reversed=False):
    doji = __create_object('DarkCloudCover')
    return doji.has_pattern(candles_df, ohlc, is_reversed)


def dragonfly_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False):
    doji = __create_object('DragonflyDoji')
    return doji.has_pattern(candles_df, ohlc, is_reversed)
