def increase(num, porcent):
    ans = num * (1 + (porcent / 100))
    format = coin(ans)
    return format


def divid(num):
    ans = num / 2
    format = coin(ans)
    return format


def twice(num):
    ans = num * 2
    format = coin(ans)
    return format


def reduce(num, porcent):
    ans = num * (1 - (porcent / 100))
    format = coin(ans)
    return format


def coin(num, coin='R$'):
    ans = f'{coin}{num:.2f}'.replace('.', ',')
    return ans


def resum(num, percentplus=False, percentmin=False):
    print('_' * 30)
    print(f'{"Summary of values":^30}')
    print('_' * 30)
    print(f'{"Price:":<30}{coin(num):>6}\n{"Twice of price":<30}{twice(num):>6}\n{"A half of the price":<30}{divid(num):>6}\n{"80% increased":<30}{increase(num, percentplus):>6}\n{"35% reduce":<30}{reduce(num, percentmin):>6}')
