# Сортировка слиянием

# Ограничение времени	2 секунды
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt

# Гоше дали задание написать красивую сортировку слиянием. Поэтому Гоше 
# обязательно надо реализовать отдельно функцию merge и функцию merge_sort.
# 
# Функция merge принимает два отсортированных массива, сливает их в один 
# отсортированный массив и возвращает его. Если требуемая сигнатура имеет 
# вид merge(array, left, mid, right), то первый массив задаётся полуинтервалом 
# [left, mid) массива array, а второй – полуинтервалом [mid, right) массива array.
# 
# Функция merge_sort принимает некоторый подмассив, который нужно отсортировать. 
# Подмассив задаётся полуинтервалом — его началом и концом. Функция должна 
# отсортировать передаваемый в неё подмассив, она ничего не возвращает.
# 
# Функция merge_sort разбивает полуинтервал на две половинки и рекурсивно вызывает 
# сортировку отдельно для каждой. Затем два отсортированных массива сливаются 
# в один с помощью merge.
# 
# Заметьте, что в функции передаются именно полуинтервалы [begin, end), то есть 
# правый конец не включается. Например, если вызвать merge_sort(arr, 0, 4), где 
# arr = [4, 5, 3, 0, 1, 2], то будут отсортированы только первые четыре элемента, 
# изменённый массив будет выглядеть как arr = [0, 3, 4, 5, 1, 2].
# 
# Реализуйте эти две функции.

def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]
    k = lf
    i = 0
    j = 0
    while (lf + i < mid and mid + j < rg):
        if (left[i] <= right[j]):
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    if lf + i < mid:
        while k < rg:
            arr[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < rg:
            arr[k] = right[j]
            j = j + 1
            k = k + 1

def merge_sort(arr, lf, rg):

    if rg - lf > 1:
        mid = (lf + rg)//2
        merge(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)
 
def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

test()

def test(result, expected):
    if result != expected:
        print(f'Ошибка!!! {result} != {expected}')
    else:
        print(f'Код работает: {result} == {expected}')

test(merge([1, 4, 9, 2, 10, 11], merge(a, 0, 3, 6)), ' ad ae af bd be bf cd ce cf')