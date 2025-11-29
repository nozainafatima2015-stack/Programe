import math

def calculate_e_power_series(x, num_terms):
    """
    Calculates e^x using the first 'num_terms' of the Taylor series expansion.
    """
    result = 0.0
    for i in range(num_terms):
        term = (x**i) / math.factorial(i)
        result += term
    return result
try:
    x_value = float(input("Enter the value for x: "))
    terms_count = int(input("Enter the number of terms for the series: "))

    approximation = calculate_e_power_series(x_value, terms_count)
    actual_value = math.exp(x_value)

    print(f"Approximation of e^{x_value} with {terms_count} terms: {approximation}")
    print(f"Actual value of e^{x_value} (using math.exp): {actual_value}")
    print(f"Difference: {abs(actual_value - approximation)}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")

