# # def fib_rec(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]
#     prev = fib_rec(n - 1)
#     return prev + [prev[-1] + prev[-2]]

# import re

# def is_sentence_palindrome(s):
#     cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
#     return cleaned == cleaned[::-1]

12. Palindrome Sentence (Ignoring Punctuation)
import re

def is_sentence_palindrome(s):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

print(is_sentence_palindrome("A man, a plan, a canal: Panama"))  # True
