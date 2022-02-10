from functools import wraps
from time import time


"""
wraps copies metadata about the inner function to the outer function. 
Without it, the decorated function object will reference the wrapper rather than the inner function. 
This is only an issue when using tools that use introspection, such as debuggers. 
For instance, if we called help on a decorated function without wraps, the help would be on the decorator instead of the inner function.
"""

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap



@timing
def f(a):
    for _ in range(a):
        i = 0
    return -1




f(100000)