import pytest

from src.challenges.longest_common_subsequence.solution import longest_common_subsequence


@pytest.mark.parametrize(argnames="case_no,", argvalues=["00"])
def test_testcases(case_no):
    input_file = f"resources/input/input{case_no}.txt"
    expected_file = f"resources/output/output{case_no}.txt"

    with open(input_file) as input_stream:
        input_size = list(map(int, next(input_stream).strip().split()))
        first_input = list(map(int, next(input_stream).rstrip().split()))
        second_input = list(map(int, next(input_stream).rstrip().split()))

    with open(expected_file) as output_stream:
        expected_result = list(map(int, next(output_stream).rstrip().split()))

    actual_result = longest_common_subsequence(first_input=first_input, second_input=second_input)
    assert actual_result == expected_result
