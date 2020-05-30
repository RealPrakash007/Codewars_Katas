def beeramid(bonus, price):
    count = 0
    cans = bonus/price
    
    while (count + 1) ** 2 <= cans:
        count += 1
        cans -= (count ** 2)
        
    return count
        