from test_framework import generic_test

# Solution help: NeetCode: https://www.youtube.com/watch?v=g9YQyYi4IQQ
def power(x: float, y: int) -> float:
    def my_pow(x, y):
        if y == 0: return 1
        if x == 0: return 0

        res = my_pow(x, y // 2)
        res *= res
        return x * res if y % 2 else res

    result = my_pow(x, abs(y))
    return 1 / result if y < 0 else result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
