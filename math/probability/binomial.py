#!/usr/bin/env python3
"""
A class for binomial distribution
"""

class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize Binomial distribution."""
        if data is None:
            if not isinstance(n, int) or n <= 0:
                raise ValueError("n must be a positive integer")
            if not isinstance(p, (int, float)) or p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = n
            self.p = p
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            self.p = 1 - (variance / mean)
            self.n = round(mean / self.p)
            self.p = mean / self.n  # Recalculate p to avoid floating-point issues

    def pmf(self, k):
        """Calculate Probability Mass Function."""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        return (
            self.combination(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        )

    def cdf(self, k):
        """Calculate Cumulative Distribution Function."""
        k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))

    @staticmethod
    def factorial(n):
        """Calculate factorial of n safely."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def combination(n, k):
        """Calculate binomial coefficient nCk."""
        if k > n or k < 0:
            return 0
        return Binomial.factorial(n) // (Binomial.factorial(k) * Binomial.factorial(n - k))

