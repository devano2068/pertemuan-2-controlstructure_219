n = int(input("masukkan nilai n untuk batas fibonacci: "))

a, b = 0, 1

print("Deret Fibonacci hingga", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b