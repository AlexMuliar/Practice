from typing import Callable, Any

from datetime import datetime, time
from functools import wraps

# TODO Create class and func decorator with and without params


class Bench:
    def __init__(self, fn: Callable=None, times=1) -> None:
        if callable(fn):
            self.fn = fn
            self.times_ = 1
        else:
            self.fn = None
            self.times_ = times


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        params = True

        if self.fn is None:
            self.fn = args[0]
            params = False

        @wraps(self.fn)
        def wrap(*args, **kwds):
            start = datetime.now()
            for _ in range(self.times_):
                res = self.fn(*args, **kwds)
            print(f"{self.fn.__name__}: {datetime.now() - start}")
            return res
        return wrap if not params else wrap(*args, **kwds)



def bench(times=1):
    params = True
    if callable(times):
        fn = times
        times = 1
        params = False

    def decorator(fn: Callable):
        @wraps(fn)
        def wrap(*args, **kwds):
            start = datetime.now()
            for _ in range(times):
                res = fn(*args, **kwds)
            print(f"{fn.__name__}: {datetime.now() - start}")
            return res
        return wrap


    if params:
        return decorator
    else:
        return decorator(fn)




# @bench(10**6)
@Bench
# @Bench(times=10**6)
def f(*args):
    return sum(args)


if __name__ == '__main__':
    r = f(1, 2, 3)
    print(r)