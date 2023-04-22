# алгоритм двоичного поиска
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# сортировка списка
def sort_list(input_list):
    return sorted(input_list)


def main():
    input_sequence = input("Введите последовательность чисел через пробел: ")
    input_list = input_sequence.split()

    # проверка соответствия условию ввода данных
    try:
        input_list = [int(x) for x in input_list]
    except ValueError:
        print("Ошибка! Необходимо вводить только целые числа, разделенные пробелом.")
        return

    # проверка на пустой список
    if not input_list:
        print("Ошибка! Список пуст.")
        return

    target_number = input("Введите любое число: ")

    # проверка соответствия условию ввода данных
    try:
        target_number = int(target_number)
    except ValueError:
        print("Ошибка! Необходимо вводить только целое число.")
        return

    sorted_list = sort_list(input_list)

    # проверка на отсутствие элементов в списке
    if not sorted_list:
        print("Ошибка! Список пуст.")
        return

    # проверка, что искомое число находится в диапазоне значений списка
    if not sorted_list[0] <= target_number <= sorted_list[-1]:
        print("Ошибка! Введенное число вне диапазона значений введенного списка.")
        return

    position = binary_search(sorted_list, target_number)
    print("Отсортированный список:", sorted_list)
    print("Позиция элемента, который меньше введенного числа: ", position)
    print("Следующий элемент, который больше или равен введённому числу: ", sorted_list[position])


if __name__ == "__main__":
    main()