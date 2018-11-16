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
    mod_name = 'candlestick.patterns.' + file_name

    if mod_name not in __builders:
        module = __load_module(mod_name)
        __builders[mod_name] = module
    else:
        module = __builders[mod_name]
    return getattr(module, class_name)


def __create_object(class_name, target):
    return __get_class_by_name(class_name)(target=target)


def bullish_hanging_man(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    bullhm = __create_object('BullishHangingMan', target)
    return bullhm.has_pattern(candles_df, ohlc, is_reversed)


def hanging_man(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    bearhm = __create_object('HangingMan', target)
    return bearhm.has_pattern(candles_df, ohlc, is_reversed)


def bearish_harami(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    bear_harami = __create_object('BearishHarami', target)
    return bear_harami.has_pattern(candles_df, ohlc, is_reversed)


def bullish_harami(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    bull_harami = __create_object('BullishHarami', target)
    return bull_harami.has_pattern(candles_df, ohlc, is_reversed)


def gravestone_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    gs_doji = __create_object('GravestoneDoji', target)
    return gs_doji.has_pattern(candles_df, ohlc, is_reversed)


def dark_cloud_cover(candles_df,
                     ohlc=__default_ohlc,
                     is_reversed=False,
                     target=None):
    dcc = __create_object('DarkCloudCover', target)
    return dcc.has_pattern(candles_df, ohlc, is_reversed)


def doji(candles_df,
         ohlc=__default_ohlc,
         is_reversed=False,
         target=None):
    doji = __create_object('Doji', target)
    return doji.has_pattern(candles_df, ohlc, is_reversed)


def doji_star(candles_df,
              ohlc=__default_ohlc,
              is_reversed=False,
              target=None):
    doji = __create_object('DojiStar', target)
    return doji.has_pattern(candles_df, ohlc, is_reversed)


def dragonfly_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    doji = __create_object('DragonflyDoji', target)
    return doji.has_pattern(candles_df, ohlc, is_reversed)


def bearish_engulfing(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('BearishEngulfing', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def bullish_engulfing(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('BullishEngulfing', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def hammer(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('Hammer', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def inverted_hammer(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('InvertedHammer', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def morning_star(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('MorningStar', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def morning_star_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('MorningStarDoji', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def piercing_pattern(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('PiercingPattern', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def rain_drop(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('RainDrop', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def rain_drop_doji(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('RainDropDoji', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def star(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('Star', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)


def shooting_star(candles_df,
                   ohlc=__default_ohlc,
                   is_reversed=False,
                   target=None):
    cndl = __create_object('ShootingStar', target)
    return cndl.has_pattern(candles_df, ohlc, is_reversed)
