input_lst = list(map(int, input("Введіть значення: ").split()))

if len(input_lst) == 0:
    print(0)
else:
    print(sum(input_lst[::2] * input_lst[-1]))