import coin
n = float(input('Type the price: R$ '))
h = coin.coin(n)
print(f'The half of {h} is R$ {coin.coin(coin.divid(n))}')
print(f'The twice of {h} is R$ {coin.coin(coin.twice(n))}')
print(f'The increased 10% in {h} is R$ {coin.coin(coin.increase(n, 10))}')
print(f'The reduce 5% in {h} is R$ {coin.coin(coin.reduce(n, 5))}')
