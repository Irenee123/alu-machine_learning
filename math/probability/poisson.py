#!/usr/bin/env python3
"""
A Class Poisson for the possion districution

"""


class Poisson:
    """
    YOu know a bunch of attributes that will one day makes sense
    """

    def __init__(self, data=None, lambtha=1.0):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of "successes"

        Args:
        k (int): number of "successes"

        Returns:
        float: PMF value for k
        """
        k = int(k)
        if k < 0:
            return 0

        e = 2.7182818285  # Approximation of e
        factorial_k = 1
        for i in range(1, k + 1):
            factorial_k *= i

        return (e**-self.lambtha) * (self.lambtha**k) / factorial_k

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of "successes"

        Args:
        k (int): number of "successes"

        Returns:
        float: CDF value for k
        """
        k = int(k)
        if k < 0:
            return 0

        cdf_value = 0
        for i in range(k + 1):
            cdf_value += self.pmf(i)

        return cdf_value
