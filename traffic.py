import random

def calculate_traffic(keywords):
    base = len(keywords) * 300
    
    # random realistic variation
    traffic = base + random.randint(500, 5000)

    return traffic
