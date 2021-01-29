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

    def display(self):
        print(f'{self.roubles},{self.kop:02}')

    def __add__(self, other):
        add_kop = self.kop + other.kop
        if add_kop >= 100:
            add_roub = add_kop // 100
            total_roub = self.roubles + other.roubles + add_roub
            add_kop %= 100
            total_kop = self.kop + other.kop + add_kop - add_roub * 100
        else:
            total_roub = self.roubles + other.roubles
            total_kop = self.kop + other.kop
        return Money(total_roub, total_kop)

    def __sub__(self, other):
        sub_kop = self.kop - other.kop
        if sub_kop < 0:
            self.roubles -= 1
            sub_kop += 100
        sub_roub = self.roubles - other.roubles
        return Money(sub_roub, sub_kop)

    def division_summs(self, other):
        return round((self.roubles * 100 + self.kop) / (other.roubles * 100 + other.kop), 2)

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
    first_sum.display()
    second_sum = Money(2, 45)
    second_sum.display()
    # roub, kop = first_sum.add(second_sum)
    # summa = Money(roub, kop)
    # summa.display()
    # first_sum.compasion(second_sum)
    # print(first_sum.multiply(1.5))
    # print(first_sum.division_float(2.5))
    # print(first_sum.division_summs(second_sum))
    # sub_roub, sub_kop = first_sum.subst(second_sum)
    # subst = Money(sub_roub, sub_kop)
    # subst.display()
    third = first_sum - second_sum
    third.display()
    print(first_sum > second_sum)
