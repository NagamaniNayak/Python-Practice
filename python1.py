# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# freq = {}
# for w in words:
#     freq[w] = freq.get(w, 0) + 1
# print(freq)
# print("Hello, World!")
# print("Hello, World!")

# print("Hello, World!")
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("minuss:", a - b)
# nums = [3, 5, 2, 8, 1]
# total = 0
# for x in nums:
#     total += x
# print("Total:", total)

# s = input("Enter text: ")
# print("Reversed:", s[::-1])

# n = int(input("Enter n: "))
# is_prime = True
# if n > 2:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
# print("Prime" if is_prime else "Not prime")
# Iterative version
# def fib_iter(n):
#     seq = [0, 1]
#     for i in range(2, n):
#         seq.append(seq[-1] + seq[-2])
#     return seq[:n]

# # Recursive version
# def fib_rec(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]
#     prev = fib_rec(n - 1)
#     return prev + [prev[-1] + prev[-2]]
# # Iterative version
# def fib_iter(n):
#     seq = [0, 1]
#     for i in range(2, n):
#         seq.append(seq[-1] + seq[-2])
#     return seq[:n]

# # Recursive version
# def fib_rec(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]
#     prev = fib_rec(n - 1)
#     return prev + [prev[-1] + prev[-2]]

# def fib_rec(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]
#     prev = fib_rec(n - 1)
#     return prev + [prev[-1] + prev[-2]]

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("radar"))  # True
# print(is_palindrome("hello"))  # False

# with open("example.txt", "r") as f:
#     lines = f.readlines()
# print("Line count:", len(line
x=0
while x<5:
    print(X)
    x+=1
    x = 0
while x < 5:
    print(x)
    x += 1
