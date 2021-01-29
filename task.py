#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу для решения задачи:
# Создать класс Money для работы с денежными суммами. Число
# должно быть представлено двумя полями:
# типа int для рублей и копеек.
# Дробная часть (копейки) при выводе на экран
# должна быть отделена от целой части запятой.
# Реализовать сложение, вычитание, деление сумм, де-ление суммы
# на дробное число, умножение на дробное число и операции сравнения.

class Money:

    def __init__(self, roubles, kop):
        self.roubles = int(roubles)
        self.kop = int(kop)

    def display(self):
        if self.kop < 10:
            print("{0},0{1}".format(self.roubles, self.kop))
        else:
            print("{0},{1}".format(self.roubles, self.kop))

    def add(self, other):
        add_kop = self.kop + other.kop
        if add_kop >= 100:
            add_roub = add_kop // 100
            total_roub = self.roubles + other.roubles + add_roub
            add_kop %= 100
            total_kop = self.kop + other.kop + add_kop
        else:
            total_roub = self.roubles + other.roubles
            total_kop = self.kop + other.kop
        return total_roub, total_kop

    def subst(self, other):
        sub_kop = self.kop - other.kop
        if sub_kop < 0:
            self.roubles -= 1
            sub_kop += 100
        sub_roub = self.roubles - other.roubles
        return sub_roub, sub_kop

    def division_summs(self, other):
        return (self.roubles*100+self.kop)/(other.roubles*100+other.kop)

    def division_float(self, numb):
        total = (self.roubles*100 + self.kop)/numb
        tot_roub //= 100
        tot_kop %= 100
        return tot_roub, tot_kop

    def multiply(self, numb):
        total = (self.roubles*100 + self.kop)*numb
        tot_roub //= 100
        tot_kop %= 100
        return tot_roub, tot_kop

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
    first_sum = Money(1, 2)
    first_sum.display()
    second_sum = Money(2, 3)
    second_sum.display()
    summa = first_sum.add(second_sum)
    print(summa)
