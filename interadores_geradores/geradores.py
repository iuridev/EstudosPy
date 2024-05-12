def my_gerador(numbers: list[int]):
    for num in numbers:
        yield num*2


for i in my_gerador(numbers=[1, 10, 40, 80]):
    print(i)
