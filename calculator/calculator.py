class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b):
        if b == 0: raise ZeroDivisionError("division by zero")
        return a / b

    def save_result_to_file(self, result, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(result))
