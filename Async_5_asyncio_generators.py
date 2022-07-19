from time import time, sleep


def gen(s):
    for i in s:
        yield i


def gen_filename():
    while True:
        pattern = 'file-{}.jpg'
        t = int(time() * 1_000)  # get milliseconds
        yield pattern.format(str(t))


for i in range(10):
    g = gen_filename()
    print(next(g))
    print(g.__next__())
    sleep(0.01)
