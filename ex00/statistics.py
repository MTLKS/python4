def ft_mean(*args: any) -> float:
    """return the mean of the given arguments"""
    return sum(args) / len(args)


def ft_median(*args: any) -> float:
    """return the median of the given arguments"""
    return sorted(args)[len(args) // 2]


def ft_quartile(*args: any) -> list[float, float]:
    """return the 25% and 75% quartile of the given arguments"""
    return [float(sorted(args)[len(args) // 4]),
            float(sorted(args)[len(args) // 4 * 3])]


def ft_std(*args: any) -> float:
    """return the standard deviation of the given arguments"""
    return ft_var(*args) ** 0.5


def ft_var(*args: any) -> float:
    """return the variance of the given arguments"""
    return sum((x - ft_mean(*args)) ** 2 for x in args) / len(args)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """print the statistics of the given arguments based on the keywords"""
    for value in kwargs.values():
        try:
            func = {"mean": ft_mean, "median": ft_median,
                    "quartile": ft_quartile, "std": ft_std, "var": ft_var}
            if value in func.keys():
                print(value + ":", func.get(value)(*args))
        except Exception:
            print("ERROR")
