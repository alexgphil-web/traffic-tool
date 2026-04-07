def calculate_traffic(keywords):
    total = 0

    for k in keywords:
        volume = k["volume"]
        ctr = 0.1   # 10%
        total += volume * ctr

    return int(total)