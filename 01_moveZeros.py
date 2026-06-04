input_lst = list(map(int, input("Введіть значення: ").split()))

result = [n for n in input_lst if n != 0] + [0] * input_lst.count(0)

print(result)