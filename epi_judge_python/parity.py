from test_framework import generic_test


def parity(x: int) -> int:
    num_of_bits = 0
    while x:
        num_of_bits += x & 1
        x >>= 1
    return num_of_bits & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
