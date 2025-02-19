#!/usr/bin/env python3
"""
A class for binomial distribution
"""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize Binomial distribution."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.p = sum(data) / (len(data) * max(data))
            self.n = round(sum(data) / self.p)
            self.p = sum(data) / (self.n * len(data))

    def pmf(self, k):
        """Calculate Probability Mass Function."""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        coef = self.factorial(self.n) // (
            self.factorial(k) * self.factorial(self.n - k)
        )
        return coef * (self.p**k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculate Cumulative Distribution Function."""
        k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))

    @staticmethod
    def factorial(n):
        """Calculate factorial of n."""
        if n == 0 or n == 1:
            return 1
        return n * Binomial.factorial(n - 1)
