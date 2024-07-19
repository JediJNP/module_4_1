from math import inf

def divide(first, second):
    res = 'wait'
    if second == 0:
        res = inf
    else:
        res = first / second
    print(res)


if __name__ == '__main__':
    divide(2, 4)
