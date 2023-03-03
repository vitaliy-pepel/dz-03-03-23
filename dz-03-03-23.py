#task26
def Sup(a, b):
    return a**b

a = int(input('Введите основание: '))
b = int(input('Введите степень: '))
print(f'{a}**{b} = {Sup(a, b)}')

#task28
def Summatration(a, b):
    if b != 0:
        return Summatration(a + 1, b - 1)
    else:
        return a

a = int(input('Введите первое слогаемое: '))
b = int(input('Введите второе слогаемое: '))
print(f'Сумма: {Summatration(a, b)}')