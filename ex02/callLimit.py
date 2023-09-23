def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that limits the number of times a function can be called
        """
        def limit_function(*args: any, **kwargs: any) -> any:
            """
            Decorator that limits the number of times a function can be called
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} call too many times")
                return None
        return limit_function
    return callLimiter
