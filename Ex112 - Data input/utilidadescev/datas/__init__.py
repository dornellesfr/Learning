from ex112.utilidadescev.coin import resum


def readmoney(num):
    while num != float:
        num = str(input('Type a number: ')).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print('Error: Type a valid number!')
        else:
            return float(num)
