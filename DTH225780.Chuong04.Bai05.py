def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def listfibo(n):
    return [fibonacci(i) for i in range(1, n + 1)]

x = int(input("Nhập vị trí N trong dãy số fibonacci:"))
result = fibonacci(x);
print(f"Giá trị vị trí N trong dãy số fibonacci {result}")

list = listfibo(x);
print(f"Toàn bộ dãy: {list}")