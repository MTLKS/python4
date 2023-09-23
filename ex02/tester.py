from callLimit import callLimit


@callLimit(3)
def f():
    """f() docstring"""
    print("f()")


@callLimit(1)
def g():
    """g() docstring"""
    print("g()")


def main():
    """main() docstring"""
    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
