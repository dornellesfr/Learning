from ex115.lib.interface import title


def arqexist(name):
    try:
        a = open(name, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def makearq(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was a error in file creation')
    else:
        print(f'Arquive created {name} with sucess')


def readfile(name):
    try:
        a = open(name, 'r')
    except:
        print('Error: NOT POSSIBLE TO READ IT')
    else:
        title('People registered')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<20}{data[1]:>5} years old')
    finally:
        a.close()


def register(arq, name='None', age='0'):
    try:
        a = open(arq, 'at')
    except:
        print('There was a error in file')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('The was a error writing in file')
        else:
            print('New register added with sucess')
