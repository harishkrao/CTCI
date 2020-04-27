n = int(input("Enter value of n: "))


class fib:
    @staticmethod
    def fibonacci(n, memo):
        if n == 1 or n == 0:
            memo.append(0)
            memo.append(1)
        print(memo)
        if len(memo) < n:
            memo.insert(n, fib.fibonacci(n - 1, memo) + fib.fibonacci(n - 2, memo))
        return memo[n]


memo = []
output = fib.fibonacci(n, memo)
print(f"Fibonacci sum of input {n} is {output}.")
