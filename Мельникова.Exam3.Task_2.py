#Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrom(word):
    if word.lower() == word[::-1].lower():
        return f'Слово является палиндромом: {word.lower()} = {word[::-1].lower()} '
    else:
        return f'Слово не является палиндромом: {word.lower()} != {word[::-1].lower()}'

print(palindrom(input('введите слово: ')))