# minimum number of coins [20,10,5,1] to give while making change
def get_minimum_coins(amount):
    coins = [20,10,5,1]
    current_coin_index = 0
    coins_counter = 0
    while amount>0:
        if coins[current_coin_index]<=amount:
            amount -= coins[current_coin_index]
            coins_counter += 1
        else:
            current_coin_index +=1
    return coins_counter

def get_minimum_coins_v2(amount):
    coins = [20,10,5,1]
    coins_counter = 0
    current_amount = amount
    for coin in coins:
        if current_amount>0:
            possible = current_amount // coin
            if possible:
                current_amount-= possible*coin
                coins_counter+= possible
    return coins_counter

print(get_minimum_coins(47))
print(get_minimum_coins_v2(47))

