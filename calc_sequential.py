import operator
import random

start_time = time.time()

operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]

for i in range(200):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op, fn = random.choice(operators)
    print("{} {} {} = {}".format(a, op, b, fn(a, b)))