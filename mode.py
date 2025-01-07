from collections import Counter

def calculate_mode(data):
    """
    Calculate the mode from a list of numerical data.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    list: A list of mode(s). If multiple values occur with the same frequency, all are returned.
    """
    if len(data) == 0:
        return None  # Return None if data list is empty

    # Count occurrences of each value
    frequency_count = Counter(data)
    
    # Find the maximum frequency
    max_frequency = max(frequency_count.values())
    
    # Extract all values with the maximum frequency
    mode = [key for key, freq in frequency_count.items() if freq == max_frequency]
    
    return mode

# Example usage:
data = [400, 500, 550, 600, 500, 500, 450, 600, 550]  # Replace with your dataset
mode_value = calculate_mode(data)

print(f"Mode(s) from Data: {mode_value}")
