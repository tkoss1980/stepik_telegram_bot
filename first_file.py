m = float(input())
r = float(input())
imt = m / ( r ** 2)
if 18.5 <= imt <= 25:
    print('Оптимальная масса')
elif imt < 18.5:
    print('Недостаточная масса')
else:
    print('Избыточная масса')
