import concurrent.futures
import functools


class uRES():
    '''result class'''
    def __init__(self, future):
        self.future = future

    def __getattr__(self, name):
        self.wait()
        return self.result.__getattribute__(name)

    def wait(self):
        '''wait for result and return it'''
        self.result = self.future.result()
        return self.result

    __call__ = lambda self: self.wait()    
    __repr__ = lambda self: self.wait()
    __str__  = lambda self: str(self.wait())

def uparallel(pool_size):
    def newdec(func):
        tpe = concurrent.futures.ThreadPoolExecutor(pool_size)
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            future = tpe.submit(func, *args, **kwargs)
            return uRES(future)
        return wrapped
    return newdec
