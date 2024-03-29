# LAB - Class 02 - Modules and Testing

**Project:** Math Series Functions

**Author:** Latherio Kidd

## Links and Resources

- [GitHub Repository](https://github.com/LatherioK0818/math-series)

### Setup

- **Environment Variables (`.env` requirements):**
  - None

#### How to Initialize/Run Your Application

- No application to run, but you can run tests using `pytest test_series.py`

# How to Use Your Library

There is no external library to use.

## Functions

### `fibonacci(n)`

Calculate the nth number in the Fibonacci series.

- `n`: An integer representing the position in the Fibonacci series.
- Returns: The nth number in the Fibonacci series.

### `lucas(n)`

Calculate the nth number in the Lucas series.

- `n`: An integer representing the position in the Lucas series.
- Returns: The nth number in the Lucas series.

### `sum_series(n, a=0, b=1)`

Calculate the nth number in a series defined by two initial values.

- `n`: An integer representing the position in the series.
- `a`: The first initial value (default is 0).
- `b`: The second initial value (default is 1).
- Returns: The nth number in the series defined by `a` and `b`.

# Tests

- **How to Run Tests:** Run the following command in your terminal:
  ```
  pytest test_series.py
  ```
- **Tests of Note:** Test all three functions: `fibonacci`, `lucas`, and `sum_series`.

#### Project Code

##### series.py

```python
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

def sum_series(n, a=0, b=1):
    """
    Calculate the nth number in a series defined by two initial values.

    :param n: An integer representing the position in the series.
    :param a: The first initial value (default is 0).
    :param b: The second initial value (default is 1).
    :return: The nth number in the series defined by a and b.
    """
    if n == 0:
        return a
    elif n == 1:
        return b

    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

![Alt text](image.png)
```
