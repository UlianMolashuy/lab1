
def myencode(message):
    itog = ''
    alfavit = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ' \
               'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' \
               '1234567890*()-=+/!@#:;'
    krok = 1
    for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto + krok
        if i in alfavit:
            itog += alfavit[new_mesto]
        else:
            itog += i
    return(itog)

def mydecode(message):
    itog = ''
    alfavit = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ' \
               'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' \
               '1234567890*()-=+/!@#:;'
    krok = -1
    for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto + krok
        if i in alfavit:  # шифруєм укр символи за допомогою зміщення на 1 вперід змінна krok
            itog += alfavit[new_mesto]
        else:
            itog += i
    return(itog)


