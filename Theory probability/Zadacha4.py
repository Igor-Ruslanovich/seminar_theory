from math import factorial

"""
В лотерее 100 билетов. Из них 2 выигрышных. 
Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
"""

P = (factorial(2) / (factorial(2)*factorial(2 - 2))) / (factorial(100) / (factorial(2)*factorial(100 - 2)))
print(f'Вероятность того, что оба билета выигрышные = {P:.5f}')
