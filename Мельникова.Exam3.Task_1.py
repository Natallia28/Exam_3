# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
def card(number):
    return '*'* (len(number)-4) + number[-4:]

print('Номер карты: ', card('1234123412341234'))