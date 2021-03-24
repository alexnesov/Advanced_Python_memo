# https://www.youtube.com/watch?v=DnKxKFXB4NQ&ab_channel=mCoding

"""
Recursive fashion, extremely inefficient.
Around 31-32 iterations the code starts to halt, it get's extremely slow.
Each number after that is twice as long as the number before.


A solution is to remember the values that were computed before.
"""

"""
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    for i in range(400):
        print(i, fib(i))
    print("done")
"""



import functools

@functools.lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    for i in range(400):
        print(i, fib(i))
    print("done")

# It goes through all the 400 of them immeditaly.


if __name__ == '__main__':

    main()