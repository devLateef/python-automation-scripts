import random as r
ages = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
r.seed(42)
rand_age = [r.choice(ages) for _ in range(119)]

print(rand_age)