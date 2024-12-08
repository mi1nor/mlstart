# project
from tools.mlstart import my_fn


def main() -> None:
    num = int(input("Число: "))
    str = input("Строка: ")

    result = my_fn(num, str)
    print(f'Результат: "{result}"')


if __name__ == "__main__":
    main()
