def calculate_median(data):
    """
    Calculate the median from a list of numerical data.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    float: The median of the data.
    """
    if len(data) == 0:
        return None  # Return None if data list is empty

    # Sort the data in ascending order
    sorted_data = sorted(data)
    
    n = len(sorted_data)
    mid = n // 2

    # If odd, return the middle element
    if n % 2 == 1:
        return sorted_data[mid]
    # If even, return the average of the two middle elements
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2

# Example usage:
data = [400, 500, 550, 600, 500, 450]  # Replace with your dataset
median_value = calculate_median(data)

print(f"Median from Data: {median_value}")
