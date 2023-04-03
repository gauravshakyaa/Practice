import timeit

my_list = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
my_tuple = (0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5)

my_dict = {}

print(timeit.timeit(stmt="{0, 1, 2, 3, 4, 5}", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
