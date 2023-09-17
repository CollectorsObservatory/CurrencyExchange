def rate_usd(usd, cad):
    return 1.36


def rate_euro(euro, cad):
    return 1.44


def rate_sterling(gbp, cad):
    return 1.63


def rate_mexican(mxn, cad):
    return 0.075


def rate_dom(dom, cad):
    return 0.025


def rate_swiss(chf, cad):
    return 1.45


def rate_japan(jpy, cad):
    return 0.0099


def rate_south_korea(won, cad):
    return 0.0010


def rate_china(cny, cad):
    return 0.20

def rate_costa_rica(crc, cad):
    return 0.0024


def rate_australia(aud, cad):
    return 0.91

def premium_rate_buy(premium_buy):
    premium_buy = rate - ((rate * 2) / 100)
    return premium_buy


def premium_rate_sell(premium_sell):
    premium_sell = rate + ((rate * 2) / 100)
    return premium_sell


def better_rate_buy(normal_buy):
    normal_buy = rate - ((rate * 2.7) / 100)
    return normal_buy


def better_rate_sell(normal_sell):
    normal_sell = rate + ((rate * 2.7) / 100)
    return normal_sell


def converter_buy(rates, amounts):
    amounts = amounts * rates - 3.5
    return amounts


def converter_sell(rates, amounts):
    amounts = amounts * rates + 3.5
    return amounts


