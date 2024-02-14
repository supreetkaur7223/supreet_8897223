import sqrt
def test_sqrt():
    input_number = 25
    expected_result = 5
    result = sqrt.calculate_square_root(input_number)

    assert result == expected_result, f"Error: The calculated square root {result} is not equal to the expected result {expected_result}"
