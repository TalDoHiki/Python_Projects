from random import randint
from time import sleep
from colorama import just_fix_windows_console
just_fix_windows_console()

print('\033[33m{:=^40}\033[m'.format(' \033[31mEven or Odd\033[33m '))
c_vic = 0
while True:
    print('\033[34m-=-\033[m'*15)
    sleep(1)
    eo = ['even','odd']
    player_ch = str(input('Do you want even or odd? ')).lower().strip().split()[0]
    if player_ch == eo[0:1]:
        eo.remove(player_ch)
    print("\033[33mThe house keeps what's left.\033[m")
    house_ch = eo[0]
    sleep(1)
    print('\033[34m-=-\033[m'*15)
    print('\033[33mThe house is thinking in a number...\033[m')
    house_n = randint(0,5)
    sleep(3)
    print('\033[31mThe house made up his mind.\033[m')
    player_n = int(input('and you? choose a number: '))
    sleep(0.5)
    print('\033[34m-=-\033[m'*15)
    print("\033[33mOk, let's see the results...\033[m")
    print(f'\033[31mThe house chose {house_n} being {house_ch}.\033[m')
    print(f'\033[32mThe player chose {player_n} being {player_ch}.\033[m')
    print('\033[34m-=-\033[m'*15)
    if (house_n + player_n)%2 == 0:
        if player_ch == 'even':
            print('\033[32mPlayer Won! adding victory!\033[m')
            c_vic += 1
            print('\033[32m-=-\033[m'*15)
        else:
            print('\033[31mHouse won.. ending session...\033[m')
            print('\033[31m-=-\033[m'*15)
            break
    else:
        if player_ch == 'odd':
            print('\033[32mPlayer Won! adding victory..\033[m')
            c_vic += 1
            print('\033[32m-=-\033[m'*15)
        else:
            print('\033[31mHouse won.. ending session...\033[m')
            print('\033[31m-=-\033[m'*15)
            break
sleep(2)
print(f"\033[35mSession ended with a total of {c_vic} consecutives victories.\033[m")
print('\033[32mCREDITS\033[m: \033[33mGitHub\033[m: \033[31m@TalDoHiki\033[m')
print('exiting...')
print('\033[33m-=-\033[m'*30)
sleep(3)
