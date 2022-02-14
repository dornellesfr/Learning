from ex115.lib.interface import *
from ex115.lib.arquive import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arqexist(arq):
    makearq(arq)

while True:
    ans = menu(['See peoples registered', 'Register a new person', 'Exit the system'])
    if ans == 1:
        # Option that list a content in file.
        readfile(arq)
    elif ans == 2:
        # Option to register a new people
        title('New Register')
        name = str(input('Name: '))
        age = readInt('Age: ')
        register(arq, name, age)
    elif ans == 3:
        print('Getting out of the program...')
        break
    else:
        print('Type a valid value')
    sleep(0.7)
