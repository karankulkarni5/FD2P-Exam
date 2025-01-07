def calculate_mean_from_ranges(ranges, frequencies):
    """
    Calculate the empirical mean from class intervals (ranges) and frequencies.

    Parameters:
    ranges (list of tuples): List of tuples representing class intervals [(lower, upper), ...].
    frequencies (list): List of frequencies corresponding to each class interval.

    Returns:
    float: The empirical mean of the data.
    """
    if len(ranges) != len(frequencies) or len(ranges) == 0:
        return None  # Return None if inputs are invalid

    total_frequency = sum(frequencies)
    weighted_sum = 0

    for i, (lower, upper) in enumerate(ranges):
        midpoint = (lower + upper) / 2  # Calculate midpoint of the interval
        weighted_sum += midpoint * frequencies[i]  # Multiply by frequency and sum up

    mean = weighted_sum / total_frequency
    return mean

# Example usage:
ranges = [(100, 200), (200, 300), (300, 400), (400, 500), (500, 600)]
frequencies = [5, 8, 12, 15, 10]  # Frequencies for each range

mean_value = calculate_mean_from_ranges(ranges, frequencies)
print(f"Empirical Mean from Ranges: {mean_value:.2f}")
