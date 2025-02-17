#Name: Farhan Khalid
#Title: TEMPERTURE SENSOR.
#Date: 2025-01-30
#Description:This program processes a list of temperatures, finds the minimum, maximum, and average, and handles invalid inputs like non-numeric values or out-of-range numbers (-50°C to 150°C).  


def temperature_sensor_program(temperatures):
    # Check if the list is empty
    if not temperatures:
        return "Error: No input provided."
    
    valid_temperatures = []

    for temp in temperatures:
        try:
            # Convert input to float
            temp = float(temp)

            # Check if it's within the valid range (-50°C to 150°C)
            if temp < -50 or temp > 150:
                return "Error: Out-of-bound value detected."

            valid_temperatures.append(temp)
        except (ValueError, TypeError):
            return "Error: Invalid input detected."

    # If we have valid temperatures, compute min, max, and average
    if valid_temperatures:
        min_temp = min(valid_temperatures)
        max_temp = max(valid_temperatures)
        avg_temp = sum(valid_temperatures) / len(valid_temperatures)
        return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp:.2f}°C"
    
    return "Error: No valid input detected."


# Test cases based on the given scenarios
test_cases = [
    ([-50], "Min: -50°C, Max: -50°C, Avg: -50.00°C"),  # BVA: Min boundary
    ([150], "Min: 150°C, Max: 150°C, Avg: 150.00°C"),  # BVA: Max boundary
    ([-49, 149], "Min: -49°C, Max: 149°C, Avg: 50.00°C"),  # BVA: Near boundaries
    ([-60, 20, 160], "Error: Out-of-bound value detected."),  # Robustness: Out of range
    ([20, "abc", 30], "Error: Invalid input detected."),  # Robustness: Non-numeric input
    ([10, "@", -40], "Error: Invalid input detected."),  # Robustness: Special characters
    ([2**31 - 1, -2**31], "Min: -2147483648°C, Max: 2147483647°C, Avg: 0.00°C"),  # Special: Very large input
    ([50, 50, 50], "Min: 50°C, Max: 50°C, Avg: 50.00°C"),  # Special: All same values
    ([], "Error: No input provided.")  # Edge case: Empty list
]

# Running the test cases and printing results
print("Running Test Cases...\n")
for idx, (input_data, expected_output) in enumerate(test_cases, 1):
    actual_output = temperature_sensor_program(input_data)
    match = "Yes" if actual_output == expected_output else "No"
    print(f"Test Case {idx}:")
    print(f"  Input: {input_data}")
    print(f"  Expected Output: {expected_output}")
    print(f"  Actual Output:   {actual_output}")
    print(f"  Match: {match}\n")


