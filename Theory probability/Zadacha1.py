import math
from math import factorial
""""
Из колоды в 52 карты извлекаются случайным образом 4 карты.
a) Найти вероятность того, что все карты – крести. 
б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
"""

n = factorial(52) / (factorial(4)*factorial(52 - 4))
m = factorial(13) / (factorial(4)*factorial(13 - 4))
print(f'Вероятность того, что все карты - крести = {m/n:.4f}')


P1 = (factorial(4) / (factorial(1)*factorial(4 - 1))) * (factorial(48) / (factorial(3)*factorial(48 - 3))) / n
P2 = (factorial(4) / (factorial(2)*factorial(4 - 2))) * (factorial(48) / (factorial(2)*factorial(48 - 2))) / n
P3 = (factorial(4) / (factorial(3)*factorial(4 - 3))) * (factorial(48) / (factorial(1)*factorial(48 - 1))) / n
P4 = factorial(4) / (factorial(4)*factorial(4 - 4)) / n
P = P1 + P2 + P3 + P4
print(f'Вероятность того, что из 4 выбранных карт из колоды, хотя бы один туз = {P:.2f}')