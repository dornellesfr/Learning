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
