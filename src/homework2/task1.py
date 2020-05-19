"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
   цена, а также количество S товара Посчитайте общую цену в рублях и копейках
   за L товаров.
"""


def total_sum(m, n, s):
    x = m * s
    y = n * s
    # write your code here
    return str(x) + " rubles " + str(y) + " kopecks"  # write return value here


if total_sum == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = '3', '5', '7'
    print(total_sum(m, n, s))
