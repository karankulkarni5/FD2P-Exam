def calculate_mean(data):
    """
    Calculate the empirical mean of a list of numerical data.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    float: The empirical mean of the data.
    """
    if len(data) == 0:
        return None  # Return None if the data list is empty

    mean = sum(data) / len(data)
    return mean

# Example usage:
data = [400, 550, 600, 500, 500]  # Replace this with your dataset
mean_value = calculate_mean(data)
print(f"Empirical Mean: {mean_value:.2f}")
