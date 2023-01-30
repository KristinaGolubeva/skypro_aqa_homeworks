def month_to_season(m):
    if m > 12:
        print('Введите, пожалуйста, число от 1 до 12, больше месяцев не бывает')
    elif m == 12 or m == 1 or m == 2:
        print('Зима')
    elif m == 3 or m == 4 or m == 5:
        print('Весна')
    elif m == 6 or m == 7 or m == 8:
        print('Лето')
    else:
        print('Осень')

month_to_season(1)


# Или можно так:

def month_to_season2(s):
    if s > 12:
        print('Введите, пожалуйста, число от 1 до 12, больше месяцев не бывает')
    elif s == 12 or s <= 2:
        print('Зима')
    elif s >= 3 and s <= 5:
        print('Весна')
    elif s >= 6 and s <= 8:
        print('Лето')
    else:
        print('Осень')

month_to_season2(12)
