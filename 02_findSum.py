input_lst = list(map(int, input("Введіть значення: ").split()))

print(sum(input_lst[::2] * input_lst[-1]))