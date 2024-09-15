from math import factorial

"""
На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
Код содержит три цифры, которые нужно нажать одновременно. 
Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?
"""


P = 1 / (factorial(10) / factorial(10 - 3))
print(f'Вероятность того, что дверь открыта с первой попытки = {P:.4f}')