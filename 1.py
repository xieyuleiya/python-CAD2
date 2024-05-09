"""
by leilei
备注：开始学习CAD
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class Calculator:
    def __init__(self):
        pass

    def multiply(self, a, b):
        return a * b


# 测试代码
if __name__ == "__main__":
    # 在此处执行测试代码
    result = add(5, 3)
    print("Addition result:", result)

    result = subtract(10, 4)
    print("Subtraction result:", result)

    calc = Calculator()
    result = calc.multiply(2, 6)
    print("Multiplication result:", result)
