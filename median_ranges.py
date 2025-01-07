def calculate_median_from_ranges(ranges, frequencies):
    """
    Calculate the median from class intervals (ranges) and frequencies.

    Parameters:
    ranges (list of tuples): List of tuples representing class intervals [(lower, upper), ...].
    frequencies (list): List of frequencies corresponding to each class interval.

    Returns:
    float: The estimated median of the data.
    """
    if len(ranges) != len(frequencies) or len(ranges) == 0:
        return None  # Return None if inputs are invalid

    # Step 1: Calculate cumulative frequencies
    cumulative_frequencies = []
    cumulative_sum = 0

    for freq in frequencies:
        cumulative_sum += freq
        cumulative_frequencies.append(cumulative_sum)

    # Step 2: Find the median class (where N/2 falls)
    total_frequency = cumulative_frequencies[-1]
    median_position = total_frequency / 2

    for i, cum_freq in enumerate(cumulative_frequencies):
        if cum_freq >= median_position:
            median_class_index = i
            break

    # Step 3: Extract class boundaries and relevant frequencies
    lower_bound = ranges[median_class_index][0]
    class_width = ranges[median_class_index][1] - ranges[median_class_index][0]

    f_m = frequencies[median_class_index]  # Frequency of median class
    f_cumulative_before = cumulative_frequencies[median_class_index - 1] if median_class_index > 0 else 0

    # Step 4: Apply the median formula
    median = lower_bound + ((median_position - f_cumulative_before) / f_m) * class_width
    return median

# Example usage:
ranges = [(100, 200), (200, 300), (300, 400), (400, 500), (500, 600)]
frequencies = [5, 8, 12, 15, 10]  # Frequencies for each range

median_value = calculate_median_from_ranges(ranges, frequencies)
print(f"Estimated Median from Ranges: {median_value:.2f}")
