from random import randint
from time import sleep
from colorama import just_fix_windows_console
just_fix_windows_console()
gt = True
print('\033[33m{:=^40}\033[m'.format(' \033[031mGuess The Number\033[33m '))
print('\033[34mTry to guess the number between 0 and 9\033[m')
sleep(1)

#Game Assets
while gt == True:
    hs = randint(0,9)
    pl = 11
    ct = 0
    lp = []
    lg = []
    lg0 = [0]
    lgr = []
    lgr0 = [0]
    ch = ''
    print('\033[33mThe house is making his decision..\033[m')
    sleep(3)
    print('\033[35mApparently the house made up his mind.\033[m')
    print('\033[35m-=-\033[m'*15)
    sleep(1)
#Player   
    while int(pl) != hs:
        pl = (input("so.. what's your bet? "))
        while pl == '' or int(pl) > 9 or int(pl) < 0:
            print('\033[33m[INVALID VALUE]\033[m')
            pl = (input("so.. what's your bet? "))
        ct += 1
        lp.append(int(pl))
        sleep(0.5)
        if int(pl) != hs:
            print('\033[31m[bzzt] Wrong answer, try again..\033[m')
        else:
            print('\033[32m[hiss] Correct answer, good.\033[m')
        sleep(0.5)
    ct -= 1
    for c in range(1,hs+1):
        lg.append(int(c))
    for c in range(9,hs-1,-1):
        lgr.append(int(c))
    lgr0.extend(lgr)
    lg0.extend(lg)
    if hs == 0:
        lg = [1,2,3,4,5,6,7,8,9,0]
        lgr = [9,8,7,6,5,4,3,2,1,0]
#Result
    print('\033[32m-=-\033[m'*30)
    print("\033[33mNow let's see the results...\033[m")
    sleep(1)
    if ct == 0:
        print('\033[32mCongratzz dude, first try! U awesome!!\033[m')
    else:
        if lp == lg or lp == lgr or lp == lg0 or lp == lgr0:
            print("\033[35mYou typed in order, don't you.\033[m")
        elif ct <= 3:
            print('\033[34mOk.. ok.. {} times. Not bad, not bad at all\033[m'.format(ct))
        elif ct <= 7:
            print('I would say an average luck for your {} tries.'.format(ct))
        elif ct <=9:
            print('\033[33mThere is a very unlucky fella.. {} tries.\033[m'.format(ct))
        else:
            print('\033[31mYou gotta be kidding right? {} tries?? bruuh.'.format(ct))
    print('\033[33m-=-\033[m'*10)
    sleep(1.5)
#Restart
    gt = False
    ch = input('\033[33mRetry?\033[m [\033[32mY\033[m/\033[31mN\033[m] ').upper().strip()[0]
    sleep(0.5)
    while ch != 'Y' and ch != 'N':
        if ch != 'Y' and ch != 'N':
            print('\033[33m[INVALID ANSWER]\033[m')
        ch = input('\033[33mRetry?\033[m [\033[32mY\033[m/\033[31mN\033[m] ').upper().strip()[0]
        sleep(0.5)
    if ch == 'Y':
        print("Ok, let's keep going then..")
        gt = True
    elif ch == 'N':
        print('Bye bye')
    print('\033[33m-=-\033[m'*30)
#End
print('\033[32mCREDITS\033[m: \033[33mGitHub\033[m: \033[31m@TalDoHiki\033[m')
print('exiting...')
sleep(3)
print('\033[33m-=-\033[m'*30)
