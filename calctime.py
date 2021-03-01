import operator
import random
import time

start_time = time.time()

operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]

for i in range(200):
    a = random.randint(1, 200)
    b = random.randint(1, 200)
    op, fn = random.choice(operators)
    print("{} {} {} = {}".format(a, op, b, fn(a, b)))


print("--- %s seconds ---" % (time.time() - start_time))