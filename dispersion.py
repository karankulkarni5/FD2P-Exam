def calculate_variance_from_ranges(ranges, frequencies):
    """
    Calculate variance and standard deviation from class intervals and frequencies.

    Parameters:
    ranges (list of tuples): List of tuples representing class intervals [(lower, upper), ...].
    frequencies (list): List of frequencies corresponding to each class interval.

    Returns:
    tuple: (variance, standard deviation) of the data.
    """
    if len(ranges) != len(frequencies) or len(ranges) == 0:
        return None  # Return None if inputs are invalid

    # Step 1: Calculate midpoints for each class
    midpoints = [(lower + upper) / 2 for lower, upper in ranges]
    
    # Step 2: Calculate the total number of data points
    total_frequency = sum(frequencies)

    # Step 3: Calculate the mean
    weighted_sum = sum(midpoint * freq for midpoint, freq in zip(midpoints, frequencies))
    mean = weighted_sum / total_frequency

    # Step 4: Calculate the variance
    squared_differences = [(midpoint - mean) ** 2 for midpoint in midpoints]
    variance_weighted_sum = sum(squared_diff * freq for squared_diff, freq in zip(squared_differences, frequencies))
    variance = variance_weighted_sum / (total_frequency - 1)  # Sample variance (N-1)

    # Step 5: Calculate standard deviation
    standard_deviation = variance ** 0.5

    return variance, standard_deviation

# Example usage:
ranges = [(100, 200), (200, 300), (300, 400), (400, 500), (500, 600)]
frequencies = [5, 8, 12, 15, 10]  # Frequencies for each range

variance, std_dev = calculate_variance_from_ranges(ranges, frequencies)
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
