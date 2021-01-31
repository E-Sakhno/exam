#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу для решения задачи:
# Создать класс Money для работы с денежными суммами. Число
# должно быть представлено двумя полями:
# типа int для рублей и копеек.
# Дробная часть (копейки) при выводе на экран
# должна быть отделена от целой части запятой.
# Реализовать сложение, вычитание, деление сумм, деление суммы
# на дробное число, умножение на дробное число и операции сравнения.

class Money:

    def __init__(self, roubles, kop):
        self.roubles = int(roubles)
        self.kop = int(kop)

    def __str__(self):
        return (f'{self.roubles},{self.kop:02}')

    def __add__(self, other):
        total = self.roubles * 100 + self.kop + other.roubles * 100 + other.kop
        total_roub = total // 100
        total_kop = total % 100
        return Money(total_roub, total_kop)

    def __sub__(self, other):
        total = self.roubles * 100 + self.kop - other.roubles * 100 - other.kop
        total_roub = total // 100
        total_kop = total % 100
        return Money(total_roub, total_kop)

    def __truediv__(self, other):
        if isinstance(other, Money):
            return round((self.roubles * 100 + self.kop) / (other.roubles * 100 + other.kop), 2)
        else:
            total = self.roubles * 100 + self.kop / other
            total_roub = total // 100
            total_kop = total % 100
            return Money(total_roub, total_kop)

    def division_float(self, numb):
        total = (self.roubles * 100 + self.kop) / numb
        tot_roub = int(total // 100)
        tot_kop = int(total % 100)
        return tot_roub, tot_kop

    def multiply(self, numb):
        total = (self.roubles * 100 + self.kop) * numb
        tot_roub = int(total // 100)
        tot_kop = int(total % 100)
        return tot_roub, tot_kop

    def __gt__(self, other):
        return self.roubles * 100 + self.kop > other.roubles * 100 + other.kop

    def __lt__(self, other):
        return self.roubles * 100 + self.kop < other.roubles * 100 + other.kop

    def __eq__(self, other):
        return self.roubles * 100 + self.kop < other.roubles * 100 + other.kop

    def __ge__(self, other):
        return self.roubles * 100 + self.kop >= other.roubles * 100 + other.kop

    def __le__(self, other):
        return self.roubles * 100 + self.kop <= other.roubles * 100 + other.kop

    def __ne__(self, other):
        return self.roubles * 100 + self.kop != other.roubles * 100 + other.kop

    def compasion(self, other):
        first = self.roubles * 100 + self.kop
        second = other.roubles * 100 + other.kop
        if first == second:
            print("Суммы равны")
        elif first > second:
            print("Первая сумма больше")
        else:
            print("Вторая сумма больше")


if __name__ == "__main__":
    first_sum = Money(1, 65)
    print(first_sum)
    second_sum = Money(2, 45)
    print(second_sum)
    third = first_sum / second_sum
    print(third)
    print(first_sum > second_sum)
