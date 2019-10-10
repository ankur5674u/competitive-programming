def rainaverage(data):
    from collections import OrderedDict
    outdict = OrderedDict()
    for (city, val) in data:
        if city in outdict:
            outdict[city] = dict(value=outdict[city]['value'] + val, count=outdict[city]['count'] + 1)
        else:
            outdict[city] = dict(value=val, count=1)

    result = [(k, v['value'] / v['count']) for k, v in outdict.items()]
    return sorted(result, key=lambda k: k[0], reverse=False)


if __name__ == '__main__':
    rainaverage([('Bombay', 848), ('Madras', 103), ('Bombay', 923), ('Bangalore', 201), ('Madras', 128)])

