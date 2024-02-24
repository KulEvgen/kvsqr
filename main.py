import math

print('Решение квадратного уравнения вида "a*x*x+b*x+c=0"')
print()
a = float(input('Введите "a": '))
b = float(input('Введите "b": '))
c = float(input('Введите "c": '))
print()
print(str(a) + '*x*x+' + str(b) + '*x+' + str(c) + '=0')
print()
d = math.pow(b,2)-4*a*c
print('D = ' + str(d))
print()
if d > 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print('X1 = ' + str(x1))
    print('X2 = ' + str(x2))
elif d == 0:
    x = (-b)/(2*a)
    print('X = ' + str(x))
else:
    print('Корней нет')