# Периметр треугольника
# Все языки	Python 3.7.3	GNU c++17 7.3
# Ограничение времени	1 секунда	0.12 секунд	0.015 секунд
# Ограничение памяти	64Mb	64Mb	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Перед сном Рита решила поиграть в игру на телефоне. Дан массив целых чисел, в котором каждый элемент обозначает длину стороны треугольника. Нужно определить максимально возможный периметр треугольника, составленного из сторон с длинами из заданного массива. Помогите Рите скорее закончить игру и пойти спать.

# Напомним, что из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник, если выполнено неравенство треугольника: c < a + b

# Разберём пример:
# даны длины сторон 6, 3, 3, 2. Попробуем в качестве наибольшей стороны выбрать 6. Неравенство треугольника не может выполниться, так как остались 3, 3, 2 —– максимальная сумма из них равна 6.

# Без шестёрки оставшиеся три отрезка уже образуют треугольник со сторонами 3, 3, 2. Неравенство выполняется: 3 < 3 + 2. Периметр равен 3 + 3 + 2 = 8.

# Формат ввода
# В первой строке записано количество отрезков n, 3≤ n≤ 10000.

# Во второй строке записано n натуральных чисел, не превосходящих 10 000, –— длины отрезков.

# Формат вывода
# Нужно вывести одно число —– наибольший периметр треугольника.

# Пример 1
# 4
# 6 3 3 2

# 8

# Пример 2
# 6
# 5 3 7 2 8 3

# 20


def perimeter(num, arr):
    for i in range(len(arr)):
        if len(arr) == num:
                arr.sort()

    for i in range(len(arr) - 3, - 1, - 1):
        if arr[i] + arr[i + 1] > arr[i + 2]:
            return arr[i] + arr[i + 1] + arr[i + 2]
    return 0

print (perimeter(6, [5, 3, 7, 2, 8, 3]))