
n = int(input("Enter value of n: "))


class fib:
    @staticmethod
    def fibonacci(n):
        memo = []
        memo.append(0)
        memo.append(1)
        for i in range(2, n+1):
            print(memo[i-1], memo[i-2])
            memo.append(memo[i-1] + memo[i-2])
        return memo[n]


output = fib.fibonacci(n)
print(f"Fibonacci sum of input {n} is {output}.")
