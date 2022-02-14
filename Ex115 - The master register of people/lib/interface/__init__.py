def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERROR: Type a int number valid, please.')
            continue
        except KeyboardInterrupt:
            print('Data not informed by user')
            return 0
        else:
            return n


def line(long=35):
    print('-' * long)


def title(msg):
    line()
    print(f'{msg:^35}')
    line()


def menu(list):
    title('Arquive System')
    c = 1
    for item in list:
        print(f'{c} - {item}')
        c += 1
    line()
    ans = readInt('Your selection: ')
    return ans