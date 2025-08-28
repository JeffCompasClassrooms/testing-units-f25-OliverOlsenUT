# Created by ChatGPT
import re
import math

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (ignoring spaces/punctuation)."""
    cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]


def factorial(n: int) -> int:
    """Compute factorial of n (non-negative)."""
    if n < 0:
        raise ValueError("Negative input not allowed")
    return math.prod(range(1, n + 1)) if n > 0 else 1


def is_prime(n: int) -> bool:
    if type(n) == float:
        raise TypeError("Floats are not accepted")
    """Check if n is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci(n: int) -> int:
    """Return nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("Negative input not allowed")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def reverse_words(s: str) -> str:
    """Reverse the words in a sentence (not characters)."""
    return " ".join(s.split()[::-1])


def gcd(a: int, b: int) -> int:
    """Greatest common divisor using Euclid’s algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)
