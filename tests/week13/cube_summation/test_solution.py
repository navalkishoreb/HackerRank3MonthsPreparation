import pytest

from src.week13.cube_summation.solution import cube_sum


@pytest.mark.parametrize(argnames="case_no,", argvalues=["05"])
def test_testcases(case_no):
    input_file = f"resources/input/input{case_no}.txt"
    expected_file = f"resources/output/output{case_no}.txt"
    actual_results = []
    with open(input_file) as input_stream:
        test_cases_count = int(next(input_stream).strip())
        for test_case in range(test_cases_count):
            first_line = list(map(int, next(input_stream).strip().split()))
            matrix_size = first_line[0]
            operations_count = first_line[1]
            operations = []
            for i in range(operations_count):
                operation = next(input_stream).strip()
                operations.append(operation)
            result = cube_sum(n=matrix_size, operations=operations)
            actual_results.extend(result)

    expected_results = []
    with open(expected_file) as input_stream:
        for line in input_stream:
            result = int(line.strip())
            expected_results.append(result)

    assert actual_results == expected_results
