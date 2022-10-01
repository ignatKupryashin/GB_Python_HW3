# Метод для красивого вывода заголовков
import math


def title(title_string):
    print("\n" + title_string + "\n")

# Задание 1: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def task_1():
    title("Задание 1: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.")
    test_list = [1, 8, 12, 4, 115, 23]
    print(f"Первоначальный список: {test_list}")

    def odd_position_sum(array):
        answer = 0
        for i in range (0, len(array)):
            if i % 2 == 0:
                answer += array[i]
        return answer
    print(f"Ответ: {odd_position_sum(test_list)}")

# Задание 2: Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# # Пример:
# #
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]


def task_2():
    title("Задание 2: Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")
    test_list = [2, 3, 5, 6]

    def multiply_pair_index(array):
        new_array = []
        for i in range(math.floor(len(array) / 2)):
            new_array.append(array[i] * array[len(array) - 1 - i])
        return new_array
    print(multiply_pair_index(test_list))


# Задание 3: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# # Пример:
# #
# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def task_3():
    title("Задание 3: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")
    test_list = [1.1, 1.2, 3.1, 5, 10.01]

    def dif_fraction_part(array):
        min_value = 1
        max_value = 0
        for i in range(len(array)):
            current_number = array[i] % 1
            if current_number != 0:
                if current_number > max_value:
                    max_value = current_number
                elif current_number < min_value:
                    min_value = current_number
        return round(max_value - min_value, 2)
    print(dif_fraction_part(test_list))


## # Задание 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# # Пример:
# # - 45 -> 101101
# # - 3 -> 11
# # - 2 -> 10
def task_4():
    title("Задание 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.")

    def from_ten_to_two(number, answer=""):
        current_number = str(number % 2)
        number = math.floor(number / 2)
        if number > 0:
            answer += from_ten_to_two(number, answer)
        answer += str(current_number)
        return answer
    question = 45
    print(f"{question} --> {from_ten_to_two(question)}")
    question = 3
    print(f"{question} --> {from_ten_to_two(question)}")
    question = 2
    print(f"{question} --> {from_ten_to_two(question)}")

# # Задание 5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def task_5():
    title("Задание 5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")
    k = 8
    k = k - 1

    def fibonachi(size, answer = [0, 1]):
            answer.append(answer[(len(answer) - 1)] + answer[(len(answer) - 2)])
            size -= 1
            if size > 0:
                return fibonachi(size, answer)
            return answer

    def negafibonachi(array):
        answer = []
        for i in range(len(array) - 1):
            answer.append((array[(len(array) - 1 - i)]) * ((-1) ** (i + 1)))
        return answer + array
    array = fibonachi(k)
    array = negafibonachi(array)
    print(array)

task_1()
task_2()
task_3()
task_4()
task_5()