import coin
n = float(input('Type the price: R$ '))
print(f'The half of {n} is R$ {coin.divid(n):.2f}')
print(f'The twice of {n} is R$ {coin.twice(n):.2f}')
print(f'The increased 10% in {n} is R$ {coin.increase(n, 10):.2f}')
print(f'The reduce 5% in {n} is R$ {coin.reduce(n, 5):.2f}')
