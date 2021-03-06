#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу для решения задачи: В списке, состоящем из целых элементов, вычислить:
# 1) номер максимального элемента списка;
# 2) произведение элементов списка, расположенных между первым и вторым нулевыми элементами.
# Преобразовать список таким образом, чтобы в первой его половине располагались элементы,
# стоявшие в нечетных позициях, а во второй половине - элементы, стоявшие в четных позициях.


if __name__ == '__main__':
    lst = [11, 25, 1, 33, 5, 12, 3, 10]
    print(f'Список целых элементов: {lst}')

    # Вывод максималього элемента списка.
    print(f'Максимальный элемент списка: {max(lst)}')

    # Вывод произведения элементов списка, расположенных между первым и вторым нулевыми элементами
    lst1 = lst[1:-1]
    umn = 1
    for i in lst1:
        umn = umn*i
    print(f'Произведения элементов списка, расположенных между первым и вторым нулевыми элементами: {umn}')

    # Преобразование списка.
    preo = []

    for i, item in enumerate(lst):
        if i % 2 != 0:
            preo.append(item)

    for i, item in enumerate(lst):
        if i % 2 == 0:
            preo.append(item)

    print(f'Преобразованный список: {preo}')

