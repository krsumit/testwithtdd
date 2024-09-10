import re
import unittest

# String Calculator Implementation
def add(numbers):
    """
    Function to calculate the sum of numbers in a string.
    
    :param numbers: A string containing numbers separated by delimiters (comma, newline, or custom).
    :return: Sum of the numbers as an integer.
    :raises: ValueError if negative numbers are present.
    """
    if not numbers:
        return 0  # Return 0 for an empty string
    
    # Check for custom delimiter
    delimiter = ","
    if numbers.startswith("//"):
        delimiter_section, numbers = numbers.split("\n", 1)
        delimiter = delimiter_section[2:]  # Extract custom delimiter
    
    # Replace newline with the delimiter for unified processing
    numbers = numbers.replace("\n", delimiter)
    
    # Split the numbers string into individual numbers
    numbers_list = [int(num) for num in numbers.split(delimiter) if num]
    
    # Check for negative numbers
    negatives = [num for num in numbers_list if num < 0]
    if negatives:
        raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
    
    return sum(numbers_list)  # Return the sum of the numbers


# Unit tests following TDD practices
class TestStringCalculator(unittest.TestCase):
    
    def test_empty_string_returns_zero(self):
        """Test case for an empty string. Should return 0."""
        self.assertEqual(add(""), 0)
    
    def test_single_number(self):
        """Test case for a single number in the string."""
        self.assertEqual(add("1"), 1)
    
    def test_two_numbers(self):
        """Test case for two comma-separated numbers."""
        self.assertEqual(add("1,2"), 3)
    
    def test_multiple_numbers(self):
        """Test case for multiple comma-separated numbers."""
        self.assertEqual(add("1,2,3,4"), 10)
    
    def test_newline_as_delimiter(self):
        """Test case to handle newlines between numbers."""
        self.assertEqual(add("1\n2,3"), 6)
    
    def test_custom_delimiter(self):
        """Test case to handle custom delimiter."""
        self.assertEqual(add("//;\n1;2"), 3)
    
    def test_negative_numbers(self):
        """Test case for negative numbers which should raise an exception."""
        with self.assertRaises(ValueError) as context:
            add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -4")


# Run the tests if this module is executed
if __name__ == "__main__":
    unittest.main()
