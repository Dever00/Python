alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

cond = int(input('Если известен открытый текст введите - 1. Если есть шифр введите - 2: '))

if(cond == 1):
    mess = input('Введите открытый текст: ').lower()
    key = int(input('Введите ключ: '))
    ckrypt = ''

    for let in mess:
        if let in alph:
            t = alph.find(let)
            new_key = (t + key) % len(alph)
            ckrypt += alph[new_key]
        else:
            ckrypt += let
    print('Зашифрованное сообщение: ', ckrypt)

elif(cond == 2):
    mess2 = input('Введите шифр: ').lower()
    key2 = int(input('Введите ключ: '))
    ckrypt2 = ''

    for let in mess2:
        if let in alph:
            t2 = alph.find(let)
            new_key = (t2 - key2) % len(alph)
            ckrypt2 += alph[new_key]
        else:
            ckrypt2 += let
    print('Открытый текст: ', ckrypt2)