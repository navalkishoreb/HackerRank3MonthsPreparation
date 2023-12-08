import os

import pytest

from src.week13.find_the_running_median.solution import running_median


@pytest.mark.parametrize(argnames="case_no,", argvalues=["00", "01", "08"])
def test_testcases(case_no):
    input_file = f"resources/input/input{case_no}.txt"
    expected_file = f"resources/output/output{case_no}.txt"

    entries = []
    with open(input_file) as input_stream:
        test_cases = int(next(input_stream).strip())
        for test_case in range(test_cases):
            entry = int(next(input_stream).strip())
            entries.append(entry)

    expected_result = []
    with open(expected_file) as output_stream:
        for line in output_stream:
            result = float(line.strip())
            expected_result.append(result)

    actual_result = running_median(entries)
    assert actual_result == expected_result
