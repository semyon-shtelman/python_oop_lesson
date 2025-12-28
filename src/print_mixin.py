class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}{tuple(arg for arg in self.__dict__.values())}"
        )
