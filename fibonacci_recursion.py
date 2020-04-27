n = int(input("Enter value of n: "))


class fib:

    @staticmethod
    def fibonacci(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib.fibonacci(n-1) + fib.fibonacci(n-2)


output = fib.fibonacci(n)
print(f"Fibonacci sum of input {n} is {output}.")
