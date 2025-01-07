def calculate_mode_from_ranges(ranges, frequencies):
    """
    Calculate the mode from class intervals (ranges) and frequencies.

    Parameters:
    ranges (list of tuples): List of tuples representing class intervals [(lower, upper), ...].
    frequencies (list): List of frequencies corresponding to each class interval.

    Returns:
    float: The estimated mode of the data.
    """
    if len(ranges) != len(frequencies) or len(ranges) == 0:
        return None  # Return None if inputs are invalid

    # Find the modal class (class with the highest frequency)
    max_frequency = max(frequencies)
    modal_class_index = frequencies.index(max_frequency)

    # Extract class boundaries and frequencies
    lower_bound = ranges[modal_class_index][0]
    class_width = ranges[modal_class_index][1] - ranges[modal_class_index][0]

    # Frequency values
    f1 = frequencies[modal_class_index]  # Frequency of the modal class
    f0 = frequencies[modal_class_index - 1] if modal_class_index > 0 else 0  # Frequency of previous class
    f2 = frequencies[modal_class_index + 1] if modal_class_index < len(frequencies) - 1 else 0  # Frequency of next class

    # Calculate mode using the formula
    mode = lower_bound + ((f1 - f0) / ((f1 - f0) + (f1 - f2))) * class_width
    return mode

# Example usage:
ranges = [(100, 200), (200, 300), (300, 400), (400, 500), (500, 600)]
frequencies = [5, 8, 12, 15, 10]  # Frequencies for each range

mode_value = calculate_mode_from_ranges(ranges, frequencies)
print(f"Estimated Mode from Ranges: {mode_value:.2f}")
