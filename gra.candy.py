# 1. Decoration
def deco(param):
    def wrapper(func):
        def inner_wrapper(*arg, **kwargs):
            print(param, arg, kwargs)
            inner_res = func(*arg, **kwargs)
            return inner_res
        return inner_wrapper
    return wrapper


@deco(param="do what you want to do")
def origin(times, add, sub, num=1):
    return times*(num + add) - sub


if __name__ == '__main__':
    print("\033[1;30;m# 1. Decoration\033[0m")
    result = origin(1, 1, 0, num=5)
    print("result =", result)


# 2. String Template .format()
if __name__ == '__main__':
    print("\033[1;30;m# 2. String Template .format()\033[0m")
    for i in range(1, 10):
        for j in range(1, i+1):
            val = "{0}*{1}={2: >2}".format(j, i, i*j)
            print(val, end='\t')
        print()
