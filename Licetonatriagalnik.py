#По подадени дължините на трите страни на триъгълник, пресметнете лицето му,
# като закръглите резултата до втората цифра след десетичната запетая.

#Формулата за пресмятане на лицето на триъгълник с дължини на страните a, b и c е:

#S = math.sqrt(p * (p - a) * (p - b) * (p - c)) , където p = (a + b + c) / 2

#Ако са подадени невалидни данни, е необходимо да изведете INVALID INPUT

#Примери:

#Входни данни                  Резултат
#1                             1.48
#3
#3

import math

aa = input()
bb = input()
cc = input()
try:
    a = float(aa)
    b = float(bb)
    c = float(cc)
except ValueError:
    print('INVALID INPUT')
else:
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        print('INVALID INPUT')
    else:
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{:.2f}".format(S))