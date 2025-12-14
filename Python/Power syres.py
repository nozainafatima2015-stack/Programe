import math

def calculate_e_power_series(x, num_terms):
    """
    Calculates e^x using the first 'num_terms' of the Taylor series expansion.
    """
    result = 0.0
    for i in range(num_terms):
        # Calculate the current term: x^i / i!
        # math.factorial(i) calculates i!
        # x**i calculates x^i
        term = (x**i) / math.factorial(i)
        result += term
    return result

# --- Main part of the program ---
# Get user input for x and the number of terms
try:
    x_value = float(input("Enter the value for x: "))
    terms_count = int(input("Enter the number of terms for the series: "))

    # Calculate the series approximation
    approximation = calculate_e_power_series(x_value, terms_count)
    actual_value = math.exp(x_value)

    # Print the results
    print(f"Approximation of e^{x_value} with {terms_count} terms: {approximation}")
    print(f"Actual value of e^{x_value} (using math.exp): {actual_value}")
    print(f"Difference: {abs(actual_value - approximation)}")

except ValueError:
    print("Invalid input. Please enter valid numbers.") 