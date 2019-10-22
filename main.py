import random


def task1():
    number_list = ", ".join([str(int(100*random.random())) for index in range(100)])
    with open("numbers.csv", "w") as file:
        file.write(number_list)


def task2():
    with open("numbers.csv", "r") as file:
        data = file.read()

    number_list = data.split(", ")
    more_than_50_count = 0
    for number in number_list:
        more_than_50 = int(number) > 50
        if more_than_50:
            more_than_50_count += 1

        print("{} {}".format(number, int(more_than_50)))

    print("more than 50 count: {}".format(more_than_50_count, ))


def task3():
    def fact(n):
        if n == 0:
            return 1
        return n * fact(n-1)

    number = None
    while number is None:
        print("input number [1..10]: ", end="")
        number = input()
        try:
            number = int(number)
            if number < 1 or number > 11:
                raise ValueError
        except ValueError:
            number = None

    print("fact({}) = {}".format(number, fact(number)))


if __name__ == '__main__':
    task1()
    task2()
    task3()
