# https://www.youtube.com/watch?v=DnKxKFXB4NQ&ab_channel=mCoding

"""
Recursive fashion, extremely inefficient.
At around 31-32 iterations the code starts to halt, it get's extremely slow.
Each number after that is twice as long as the number before.


A solution is to remember the values that were computed before.
"lru" = "least recently used"


The data cached is the data that is returned and the data as input parameter (argument)
Whenever we use the function again with the same arguments it's gonna
get the data from the storage instead from the function.
As long as the argument don't change, the result will be instant
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