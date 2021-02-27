
if __name__ == '__main__':
    # 1 зад
    at = 'Иван '
    ad = '75'
    print(at + ad)
    name = input('Как вас зовут?')
    surname = input(" Сколько вам лет?")
    print(name + surname)
    #2 зад
    import math
    d = int(input('Введите количество секунд'))
    ho = 3600
    hours = math.floor(d/ho)
    minute = math.floor((d - (hours*ho))/60)
    second = d - ((hours * ho) + (minute*60))
    print('{0}:час;{1}:минут;{2}:секунд'.format(hours,minute,second))
    #3зад
    str1 = input('Введите число')
    str2 = str1 + str1
    str3 = str1 + str2
    print(int(str1) + int(str1 + str1) + int(str1 + str2))
    #4 зад Сам решить не смог


# a = int(input())
# m = a%10
# a = a//10
# while a > 0:
#     if a%10 > m:
#         m = a%10
#     a = a//10
# print(m)
#  5 зад
    profit = int(input('Введите количество выручки'))
    costs = int(input('Введите количество издежек'))
    ter = profit - costs
    if ter < 0:
        print('Убыток составляет: '+ str(ter))
    else:
        print('Прибыль составила:' + str(ter))
    if ter > 0:
        rentTer = round(ter/profit*100)
        print('Рентабильность выручки составляет:' + str(rentTer))
        staff = int(input('Введите количество сотрудников'))
        staffProf = ter/staff
        staffProf = float('{:.2f}'.format(staffProf))
        if ter > 0:
            print('Прибыль фирмы в расчете на одного сотрудника составляет:' + str(staffProf))
    # 6 зад
"""А здесь что то новое"""