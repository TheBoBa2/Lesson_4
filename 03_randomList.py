import random

random_lst = []
amount = int(random.randint(3, 10))

while amount > 0:
    random_lst.append(random.randint(1, 10))
    amount -= 1

result = [random_lst[0], random_lst[2], random_lst[-2]]

print(random_lst, " == ", result)
