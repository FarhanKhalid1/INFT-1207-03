#Name: Farhan Khalid
#Title: TEMPERTURE SENSOR.
#Date: 2025-02-16
#Description:This program processes a list of temperatures, finds the minimum, maximum, and average, and handles invalid inputs like non-numeric values or out-of-range numbers (-50°C to 150°C).

import unittest
from ICE3.src.temperture_sensor import temperature_sensor_program


class TestTemperatureSensor(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(
            temperature_sensor_program([20, 30, 40]),
            "Min: 20.0°C, Max: 40.0°C, Avg: 30.00°C"
        )

    def test_single_value(self):
        self.assertEqual(
            temperature_sensor_program([25]),
            "Min: 25.0°C, Max: 25.0°C, Avg: 25.00°C"
        )

    def test_empty_input(self):
        self.assertEqual(
            temperature_sensor_program([]),
            "Error: No input provided."
        )

    def test_invalid_input(self):
        self.assertEqual(
            temperature_sensor_program([10, 'a', 20]),
            "Error: Invalid input detected."
        )

    def test_out_of_bound_value(self):
        self.assertEqual(
            temperature_sensor_program([200]),
            "Error: Out-of-bound value detected."
        )

    def test_valid_range(self):
        self.assertEqual(
            temperature_sensor_program([10, -40, 100]),
            "Min: -40.0°C, Max: 100.0°C, Avg: 23.33°C"
        )

    def test_large_values(self):
        # Test case for very large values
        self.assertEqual(
            temperature_sensor_program([2 ** 31 - 1, -2 ** 31]),
            "Error: Out-of-bound value detected."  # Adjusted for the out-of-bound check
        )

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()

