def divide(first, second):
    res = 'wait'
    if second == 0:
        res = 'Ошибка'
    else:
        res = first / second
    print(res)



if __name__ == '__main__':
    divide(2, 3)