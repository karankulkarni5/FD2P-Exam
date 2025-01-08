import scipy.stats as stats

def calculate_quantile(nominal_level, mean=0, std_dev=1):
    """
    Calculate the quantile of a normal distribution.

    Parameters:
    - nominal_level: The cumulative probability (e.g., 0.95 for the 95th percentile).
    - mean: Mean of the normal distribution (default is 0).
    - std_dev: Standard deviation of the normal distribution (default is 1).

    Returns:
    - The quantile value corresponding to the nominal level.
    """
    quantile = stats.norm.ppf(nominal_level, loc=mean, scale=std_dev)
    return quantile

# Example Usage
nominal_level = 0.95  # 95th percentile
mean = 0              # Mean of the distribution
std_dev = 1           # Standard deviation

quantile_value = calculate_quantile(nominal_level, mean, std_dev)
print(f"The {nominal_level*100}th percentile is: {quantile_value}")