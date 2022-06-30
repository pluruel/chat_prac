class Builder:
    def __init__(self, f) -> None:
        self.func = f

    def __call__(self, *args, **kwds):
        self.func(*args, **kwds)
        return self
