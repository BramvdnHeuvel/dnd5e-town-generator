def cached_property(func):
    fname = func.__name__

    def exec(self):
        val = getattr(self, f'__{fname}', None)
        if val is not None:
            return val

        x = func(self)

        setattr(self, f'__{fname}', x)
        return x

    return property(exec)

