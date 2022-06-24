import fibo as fb
import sys

# l = fibo.fib2(100)
# l = fb.fib2(100)
# print(l)

from fibo import fib2 as f2


def main():
    print(sys.argv)
    value = int(sys.argv[1])
    l = fb.fib2(value)
    print(l)

if __name__ == "__main__":
    main()