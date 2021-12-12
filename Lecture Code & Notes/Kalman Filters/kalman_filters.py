import numpy as np
from math import *


def gaussian(x, mu, sigma2):
    """ Calculate probability of X using Mean Mu and variance sigma
	"""
    # Code referenced from: https://gatech.instructure.com/courses/213570/pages/8-maximize-gaussian?module_item_id=1890816
    return 1 / sqrt(2.0 * pi * sigma2) * exp(-0.5 * (x - mu) ** 2 / sigma2)


def multiply_gaussians(mu1, mu2, var1, var2):
    """ Given two means (mu1, mu2) and two variance terms (sigma1, sigma2)
        calculate the the mean and variance of the new gaussian
    """

    mu_prime = (1.0 / (var1 + var2)) * (var2 * mu1 + var1 * mu2)
    sigma_prime = 1.0 / ((1.0 / var1) + (1.0 / var2))

    return mu_prime, sigma_prime


# multiply_gaussians(10, 13, 8, 2)


def predict(mu1, mu2, var1, var2):
    """ Generate predictions for KF
    """
    mu_prime = mu1 + mu2
    sigma_prime = var1 + var2

    return mu_prime, sigma_prime


predict(10, 12, 4, 4)

measurements = [5, 6, 7, 9, 10]
motion = [1, 1, 2, 1, 1]
measurement_sig = 4
motion_sig = 2
mu = 0
sig = 0.00000001  # 1000

for i in range(len(measurements)):
    # Use the measurement as the the mean (mu2)
    # Measurement info is used in the update step
    [mu, sig] = multiply_gaussians(mu, measurements[i], sig, measurement_sig)
    print(f"Update step: {[mu, sig]}")
    # Motion info is used in the prediction step
    [mu, sig] = predict(mu, motion[i], sig, motion_sig)
    print(f"Update step: {[mu, sig]}")
