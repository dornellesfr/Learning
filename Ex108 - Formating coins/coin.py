def increase(num, porcent):
    ans = num * (1 + (porcent / 100))
    return ans


def divid(num):
    ans = num / 2
    return ans


def twice(num):
    ans = num * 2
    return ans


def reduce(num, porcent):
    ans = num * (1 - (porcent / 100))
    return ans


def coin(num, coin='R$'):
    ans = f'{coin}{num:.2f}'.replace('.', ',')
    return ans
