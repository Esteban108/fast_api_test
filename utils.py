from multiprocessing import Process


class MyProds(Process):
    __process_running__ = []

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon, args=args, kwargs=kwargs)

        self.__process_running__.append(self)


def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)

        return repl

    return layer


@parametrized
def process_func(func, module_name):
    """start a daemon thread """

    def wrapper(*args, **kwargs):
        p = MyProds(target=func, daemon=True, args=args, kwargs=kwargs)
        p.module = args[0]
        p.module_name = module_name
        p.start()

    return wrapper


def op_stop_process(num1, module_name):
    for p in MyProds.__process_running__:
        if hasattr(p, "module"):
            if p.module == num1:
                if p.module_name == module_name:
                    p.terminate()
                    return True
    return False

