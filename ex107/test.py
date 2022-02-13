import coin
n = float(input('Type the price: R$ '))
print(f'The half of {n} is R$ {moeda.divid(n):.2f}')
print(f'The twice of {n} is R$ {moeda.twice(n):.2f}')
print(f'The increased 10% in {n} is R$ {moeda.increase(n, 10):.2f}')
print(f'The reduce 5% in {n} is R$ {moeda.reduce(n, 5):.2f}')
