def calculate_quantile_from_ranges(ranges, frequencies, alpha):
    """
    Calculate the quantile for a given alpha from class intervals (ranges) and frequencies.

    Parameters:
    ranges (list of tuples): List of tuples representing class intervals [(lower, upper), ...].
    frequencies (list): List of frequencies corresponding to each class interval.
    alpha (float): The quantile level (e.g., 0.05 for 5th percentile).

    Returns:
    float: The estimated quantile value.
    """
    if len(ranges) != len(frequencies) or len(ranges) == 0 or alpha < 0 or alpha > 1:
        return None  # Return None for invalid inputs

    # Step 1: Calculate cumulative frequencies
    cumulative_frequencies = []
    cumulative_sum = 0
    for freq in frequencies:
        cumulative_sum += freq
        cumulative_frequencies.append(cumulative_sum)

    total_frequency = cumulative_frequencies[-1]
    target_position = alpha * total_frequency

    # Step 2: Find the quantile class (where target_position falls)
    for i, cum_freq in enumerate(cumulative_frequencies):
        if cum_freq >= target_position:
            quantile_class_index = i
            break

    # Step 3: Extract class boundaries and relevant frequencies
    lower_bound = ranges[quantile_class_index][0]
    class_width = ranges[quantile_class_index][1] - ranges[quantile_class_index][0]
    f_cumulative_before = cumulative_frequencies[quantile_class_index - 1] if quantile_class_index > 0 else 0
    f_class = frequencies[quantile_class_index]

    # Step 4: Apply the quantile formula
    quantile = lower_bound + ((target_position - f_cumulative_before) / f_class) * class_width
    return quantile

# Example usage:
ranges = [(100, 200), (200, 300), (300, 400), (400, 500), (500, 600)]
frequencies = [5, 8, 12, 15, 10]  # Frequencies for each range

q_05 = calculate_quantile_from_ranges(ranges, frequencies, 0.05)
q_95 = calculate_quantile_from_ranges(ranges, frequencies, 0.95)

print(f"5th Quantile (q^0.05): {q_05:.2f}")
print(f"95th Quantile (q^0.95): {q_95:.2f}")
