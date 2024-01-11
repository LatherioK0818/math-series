def fibonacci(n):
    """
    Calculate the nth number in the Fibonacci series.

    :param n: An integer representing the position in the Fibonacci series.
    :return: The nth number in the Fibonacci series.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
def lucas(n):
    """
    Calculate the nth number in the Lucas series.

    :param n: An integer representing the position in the Lucas series.
    :return: The nth number in the Lucas series.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1

    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
