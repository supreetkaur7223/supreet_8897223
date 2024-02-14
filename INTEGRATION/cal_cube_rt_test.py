import cubert
def test_cube_root():
  input_number = 64
  expected_result = 4
  result = cubert.calculate_cube_root(input_number)

  assert result == expected_result, f"Error: The calculated cube root {result} is not equal to the expected result {expected_result}"

