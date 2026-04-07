def calculate_traffic(keywords):
    total = 0

    for k in keywords:
        volume = k["volume"]
        ctr = 0.1

        total += volume * ctr

    # ✅ minimum traffic
    if total == 0:
        total = 500

    return int(total)
