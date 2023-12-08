import pytest

from src.week13.journey_to_the_moon.solution import journey_to_the_moon


@pytest.mark.parametrize(argnames="case_no,", argvalues=["00", "13"])
def test_testcases(case_no):
    input_file = f"resources/input/input{case_no}.txt"
    expected_file = f"resources/output/output{case_no}.txt"

    with open(input_file) as input_stream:
        first_line = list(map(int, next(input_stream).strip().split()))
        number_of_astronauts = first_line[0]
        number_of_pairs = first_line[1]
        astronaut = []

        for pair in range(number_of_pairs):
            entry = list(map(int, next(input_stream).strip().split()))
            astronaut.append(entry)

    with open(expected_file) as expected_stream:
        expected_result = int(next(expected_stream).strip())

    actual_result = journey_to_the_moon(n=number_of_astronauts, astronaut=astronaut)
    assert actual_result == expected_result
