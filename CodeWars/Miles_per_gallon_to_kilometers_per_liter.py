def converter(mpg):
    mpg = int(mpg)
    """ 1 Imperial Gallon = 4.54609188 litres 
    1 Mile = 1.609344 kilometres"""
    # kilometr per liter will be
    kpl = 1.609344/4.54609188
    # to convert we have to multiply mpg and kpl
    res = mpg*kpl
    #? then we will format it to show just 2 decimal and round it
    tot = "{:.2f}".format(round(res, 2))
    # and return result as float
    return float(tot)
