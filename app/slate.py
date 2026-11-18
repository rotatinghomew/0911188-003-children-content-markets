def next_slots(meters, count):
    eligible = [key for key, row in meters.items() if row['eligible']]
    return sorted(eligible, key=lambda key: (-meters[key]['seconds'], key))[:count]
