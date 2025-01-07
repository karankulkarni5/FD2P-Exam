import numpy as np
from scipy.stats import rankdata

def spearman_rank_correlation(X, Y):
    """
    Calculate Spearman's Rank Correlation Coefficient between two variables X and Y.

    Parameters:
    X (list or array): Values of variable X.
    Y (list or array): Values of variable Y.

    Returns:
    float: Spearman's rank correlation coefficient.
    """
    # Step 1: Calculate the ranks of X and Y
    rank_X = rankdata(X)
    rank_Y = rankdata(Y)

    # Step 2: Calculate rank differences and their squares
    d = rank_X - rank_Y
    d_squared = np.sum(d ** 2)

    # Step 3: Apply Spearman's formula
    n = len(X)
    spearman_corr = 1 - (6 * d_squared) / (n * (n**2 - 1))

    return spearman_corr

# Example usage:
X = np.array([1,3,4,2])
Y = np.array([4,1,2,3])

result = spearman_rank_correlation(X, Y)
print(f"Spearman's Rank Correlation Coefficient: {result:.2f}")
