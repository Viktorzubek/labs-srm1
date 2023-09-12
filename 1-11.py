def main():
    while True:
        print("Оберіть завдання:")
        print("1. Обчислення площі та периметру прямокутника")
        print("2. Обчислення середнього геометричного")
        print("3. Обчислення площі та периметру прямокутника за координатами вершин")
        print("4. Перевірка на парність числа")
        print("5. Перевірка висловлень")
        print("6. Перевірка кольору шахової дошки")
        print("7. Перевірка можливості ферзя перейти на інше поле")
        print("8. Виведення цілих чисел між A і B")
        print("9. Знаходження числа, отриманого при читанні N справа наліво")
        print("10. Віднімання 18 від елементів масиву, які більші середнього значення")
        print("11. Перевірка на простоту числа")
        print("0. Вийти з програми")

        choice = input("Ваш вибір: ")

        if choice == '0':
            break
        elif choice == '1':
            calculate_rectangle()
        elif choice == '2':
            calculate_geometric_mean()
        elif choice == '3':
            calculate_rectangle_from_coordinates()
        elif choice == '4':
            check_even_odd()
        elif choice == '5':
            check_statements()
        elif choice == '6':
            check_chessboard_color()
        elif choice == '7':
            check_queen_move()
        elif choice == '8':
            print_numbers_between_A_and_B()
        elif choice == '9':
            reverse_number()
        elif choice == '10':
            subtract_18_from_above_average()
        elif choice == '11':
            check_prime_number()
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


def calculate_rectangle():
    a = float(input("Введіть довжину сторони a: "))
    b = float(input("Введіть довжину сторони b: "))

    s = a * b
    p = 2 * (a + b)

    print("Площа прямокутника:", s)
    print("Периметр прямокутника:", p)


def calculate_geometric_mean():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))

    geometric_mean = (a * b) ** 0.5

    print("Середнє геометричне:", geometric_mean)


def calculate_rectangle_from_coordinates():
    x1, y1 = map(int, input("Введіть координати вершини (x1, y1): ").split())
    x2, y2 = map(int, input("Введіть координати вершини (x2, y2): ").split())

    width = abs(x2 - x1)
    height = abs(y2 - y1)

    s = width * height
    p = 2 * (width + height)

    print("Площа прямокутника:", s)
    print("Периметр прямокутника:", p)


def check_even_odd():
    a = int(input("Введіть ціле число a: "))

    if a % 2 == 0:
        print("Число парне.")
    else:
        print("Число непарне.")


def check_statements():
    a = int(input("Введіть ціле число a: "))
    b = int(input("Введіть ціле число b: "))
    c = int(input("Введіть ціле число c: "))

    is_a_less_than_b_less_than_c = a < b < c
    is_at_least_one_positive = a > 0 or b > 0 or c > 0
    is_exactly_one_positive = (a > 0 and b <= 0 and c <= 0) or (a <= 0 and b > 0 and c <= 0) or (a <= 0 and b <= 0 and c > 0)

    print("a < b < c:", is_a_less_than_b_less_than_c)
    print("Хоча б одне додатне число:", is_at_least_one_positive)
    print("Рівно одне додатне число:", is_exactly_one_positive)


def check_chessboard_color():
    x = int(input("Введіть координату x: "))
    y = int(input("Введіть координату y: "))

    is_white = (x + y) % 2 == 0

    print("Поле з координатами ({}, {}) біле: {}".format(x, y, is_white))


def check_queen_move():
    x1, y1 = map(int, input("Введіть координати поля (x1, y1): ").split())
    x2, y2 = map(int, input("Введіть координати поля (x2, y2): ").split())

    can_queen_move = (x1 == x2) or (y1 == y2) or (abs(x1 - x2) == abs(y1 - y2))

    print("Ферзь може перейти з поля ({}, {}) на поле ({}, {}): {}".format(x1, y1, x2, y2, can_queen_move))


def print_numbers_between_A_and_B():
    A = int(input("Введіть ціле число A: "))
    B = int(input("Введіть ціле число B: "))

    if A < B:
        for i in range(A, B + 1):
            print(i)
    else:
        print("A повинно бути менше за B.")


def reverse_number():
    N = int(input("Введіть ціле число N: "))
    reversed_N = int(str(N)[::-1])

    print("Число, отримане при читанні N справа наліво:", reversed_N)


def subtract_18_from_above_average():
    numbers = [int(x) for x in input("Введіть числа, розділені пробілами: ").split()]
    average = sum(numbers) / len(numbers)

    for i in range(len(numbers)):
        if numbers[i] > average:
            numbers[i] -= 18

    print("Результат:", numbers)


def check_prime_number():
    N = int(input("Введіть ціле число N: "))

    if N > 1:
        is_prime = True
        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                is_prime = False
                break
        print(is_prime)
    else:
        print("N має бути більше за 1.")


if __name__ == "__main__":
    main()
