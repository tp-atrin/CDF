import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def cumulative_distribution_function(data):
    data.sort()  # Sort the data in ascending order
    n = len(data)  # Number of data points

    # Calculate the probabilities for each data point
    probabilities = np.arange(1, n + 1) / n

    # Plot the cumulative distribution function
    plt.plot(data, probabilities, marker='o')
    plt.xlabel('Data')
    plt.ylabel('Cumulative Probability')
    plt.title('Cumulative Distribution Function')
    plt.grid(True)
    plt.show()

# Example usage: Plot CDF for a set of random data points from a normal distribution
mu = 0  # Mean of the normal distribution
sigma = 1  # Standard deviation of the normal distribution
data = np.random.normal(mu, sigma, 100)  # Generate 100 random data points from the normal distribution
cumulative_distribution_function(data)

