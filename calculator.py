"""PyCharm очень ругается на переменную "input", и я с ним согласен,
 поэтому в функции "main(input: str)" заменил на "input_user" """


def main(input_user: str):
    # Преобразуем введённую строку в список. В случае неудачи исключение будет обработано
    try:
        list_input = input_user.split(' ')
        a, b = int(list_input[0]), int(list_input[2])

        # Создаём словарь с арифметическими символами в качестве ключей и соответствующих мини-функций в качестве значений
        operations = {
            '+': lambda: a + b,
            '-': lambda: a - b,
            '*': lambda: a * b,
            '/': lambda: a // b
        }

        # Проверяем корректность ввода (три элемента через пробел), введённые числа (от 1 до 10), соответствие арифметического символа
        if len(list_input) != 3 or a not in range(1, 11) or b not in range(1, 11) or list_input[1] not in operations:
            return 'throws Exception'
        else:
            return operations[list_input[1]]()

    # обрабатываем любое непредвиденное исключение
    except:
        return 'throws Exception'


# Выводим и вызываем функцию одновременно
print(main(input()))
