#!/usr/bin/env python3
"""
This annoying class
"""


class Normal:
    """
    A class that represents a normal distribution.
    """

    def __init__(self, data=None, mean=0.0, stddev=1.0):
        """
        Initialize the Normal distribution.
        Args:
            data
            mean
            stddev
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (
                sum((x - self.mean) ** 2 for x in data) / len(data)
            ) ** 0.5

    def z_score(self, x):
        """Calculate the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score."""
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculate the Probability Density Function"""
        coefficient = 1 / (self.stddev * (2 * self.pi) ** 0.5)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        return coefficient * self.e**exponent

    def cdf(self, x):
        """
        Calculates the value of the
        CDF for a given x-value
        """
        mean = self.mean
        stddev = self.stddev
        pi = 3.1415926536
        value = (x - mean) / (stddev * (2 ** (1 / 2)))
        val = value - ((value**3) / 3) + ((value**5) / 10)
        val = val - ((value**7) / 42) + ((value**9) / 216)
        val *= 2 / (pi ** (1 / 2))
        cdf = (1 / 2) * (1 + val)
        return cdf

    @property
    def pi(self):
        """Approximation of pi."""
        return 3.1415926535897932

    @property
    def e(self):
        """Approximation of e."""
        return 2.7182818284590452
