# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 09:12:05 2020

@author: Dominik
"""

from collections import OrderedDict
def write_LICZBY_RZYMSKIE(num):

    LICZBY_RZYMSKIE = OrderedDict()
    LICZBY_RZYMSKIE[1000] = "M"
    LICZBY_RZYMSKIE[500] = "D"
    LICZBY_RZYMSKIE[100] = "C"
    LICZBY_RZYMSKIE[50] = "L"
    LICZBY_RZYMSKIE[10] = "X"
    LICZBY_RZYMSKIE[5] = "V"
    LICZBY_RZYMSKIE[1] = "I"

    def LICZBY_RZYMSKIE_num(num):
        for r in LICZBY_RZYMSKIE.keys():
            x, y = divmod(num, r)
            yield LICZBY_RZYMSKIE[r] * x
            num -= (r * x)
            if num > 0:
                LICZBY_RZYMSKIE_num(num)
            else:
                break

    return "".join([a for a in LICZBY_RZYMSKIE_num(num)])
num = int(input("Podaj liczbę do przekształcenia na liczby rzymskie: "))
print ("Liczba" ,num, "w systemie rzymskim to: ",write_LICZBY_RZYMSKIE(num))
