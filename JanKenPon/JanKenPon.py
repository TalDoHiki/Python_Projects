from random import choice
from colorama import just_fix_windows_console
from time import sleep
just_fix_windows_console()
colors = {
    'clear':'\033[m',
    'white':'\033[30m',
    'red':'\033[31m',
    'green':'\033[32m',
    'yellow':'\033[33m',
    'blue':'\033[34m',
    'purple':'\033[35m',
    'cian':'\033[36m',
    'grey':'\033[37m'
}
jkp = ['rock', 'paper', 'scissors']
print('{}-=-{}'.format(colors['yellow'],colors['clear'])*50)

print("{}Let's play JanKenPon!!!{}".format(colors['blue'],colors['clear']))
sleep(1)
print("{}..rock, paper or scissors..{}".format(colors['cian'],colors['clear']))

print('{}-=-{}'.format(colors['yellow'], colors['clear'])*10)
gt = True
while gt == True:
    stg = True
    sleep(2)
    print('{}The house is choosing...{}'.format(colors['red'],colors['clear']))
    sleep(3)
    hs = choice(jkp)
    print('{}Apparently the house made up his mind.{}'.format(colors['yellow'],colors['clear']))
    sleep(1)
    pl = str(input("{}shhh.. and you? What do you will pick (the house doesn't know..): {}".format(colors['grey'],colors['clear']))).lower().strip().split()[0]
    sleep(1)
    print('JAN..')
    sleep(1)
    print('KEN..')
    sleep(1)
    print('PON!!!')
    print('{}-=-{}'.format(colors['yellow'], colors['clear'])*10)
    print('{}The house chose {}{}.'.format(colors['yellow'] ,hs ,colors['clear']))
    print('{}The player chose {}{}.'.format(colors['yellow'], pl, colors['clear']))
    print('{}-=-{}'.format(colors['yellow'], colors['clear'])*10)
    sleep(1)
    if hs == pl:
        print("{}Damn, you two has picked the same thing.. Let's do it again!{}".format(colors['yellow'],colors['clear']))
    elif hs == 'scissors' and pl == 'rock':
        print("{}Congratzz dude!! You won!!{}".format(colors['green'],colors['clear']))
    elif hs == 'rock' and pl == 'scissors':
        print('{}Yep.. You lost, better luck next time..{}'.format(colors['red'],colors['clear']))
    elif hs == 'paper' and pl == 'rock':
        print('{}Yep.. You lost, better luck next time..{}'.format(colors['red'],colors['clear']))
    elif hs == 'rock' and pl == 'paper':
        print('{}Congratzz dude!! You won!!{}'.format(colors['green'],colors['clear']))
    elif hs == 'paper' and pl == 'scissors':
        print('{}Congratzz dude!! You won!!{}'.format(colors['green'],colors['clear']))
    elif hs == 'scissors' and pl == 'paper':
        print('{}Yep.. You lost, better luck next time..{}'.format(colors['red'],colors['clear']))
    else:
        print('{}[INVALID PICK]{}'.format(colors['red'],colors['clear']))
    sleep(2)
    print('{}-=-{}'.format(colors['yellow'], colors['clear'])*10)
    stg = False
    if stg == False:
        gtc = int(input('{}Retry?{} {}1-Yes{} / {}0-No{}: '.format(colors['yellow'],colors['clear'],colors['green'],colors['clear'],colors['red'],colors['clear'])))
        if gtc == 0:
            print('Bye bye!')
            gt = False
        else:
            print("Noice! Let's keep going then..")
        print('{}-=-{}'.format(colors['yellow'], colors['clear'])*10)
print('[{}CREDITS{}: {}GitHub{}: {}@TalDoHiki{}]'.format(colors['green'], colors['clear'], colors['yellow'],colors['clear'],colors['red'],colors['clear']))
print('exiting...')
sleep(3)
