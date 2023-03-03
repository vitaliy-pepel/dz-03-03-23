#task26
def Sup(a, b):
    if b == 1: 
        return a
    return a * Sup(a, b - 1)

a = int(input('Введите основание: '))
b = int(input('Введите степень: '))
print(f'{a}**{b} = {Sup(a, b)}')

#task28
def Summatration(a, b):
    if b != 0:
        return Summatration(a + 1, b - 1)
    return a

a = int(input('Введите первое слогаемое: '))
b = int(input('Введите второе слогаемое: '))
print(f'Сумма: {Summatration(a, b)}')
