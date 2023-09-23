def square(x: int | float) -> int | float:
    """square function"""
    return x * x


def pow(x: int | float) -> int | float:
    """pow function"""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer function"""
    count = 0

    def inner() -> float:
        """inner function"""
        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result

    return inner
