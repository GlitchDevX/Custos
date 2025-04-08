class SingletonMeta(type):
    """
    A metaclass that implements the singleton design pattern.
    This metaclass ensures that a class has only one instance and provides a global point of access to it.
    """

    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]
    