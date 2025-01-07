
# Пример 1: O(1) — Константная сложность
# Доступ к элементу списка по индексу
def get_element(lst, index):
    return lst[index]

lst = [1, 2, 3, 4, 5]
print(get_element(lst, 2))  # O(1)


# Пример 2: O(n) — Линейная сложность
# Сумма всех элементов списка
def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

lst = [1, 2, 3, 4, 5]
print(sum_list(lst))  # O(n)