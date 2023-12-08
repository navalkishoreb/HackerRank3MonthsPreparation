import pytest

from src.week13.roads_and_libraries.solution import roads_and_libraries


@pytest.mark.parametrize(argnames="case_no,", argvalues=[ "12"])
def test_testcases(case_no):
    input_file = f"resources/input/input{case_no}.txt"
    expected_file = f"resources/output/output{case_no}.txt"

    entries = []
    with open(input_file) as input_stream:
        test_cases = int(next(input_stream).strip())
        for test_case in range(test_cases):
            entry = list(map(int, next(input_stream).strip().split()))
            cities_count = entry[0]
            edges = entry[1]
            library_cost = entry[2]
            road_cost = entry[3]
            connections = []
            for i in range(edges):
                edge = list(map(int, next(input_stream).strip().split()))
                connections.append(edge)

            entries.append((cities_count, library_cost, road_cost, connections))

    expected_result = []
    with open(expected_file) as output_stream:
        for line in output_stream:
            result = float(line.strip())
            expected_result.append(result)

    actual_result = []
    for entry in entries:
        result = roads_and_libraries(n=entry[0], c_lib=entry[1], c_road=entry[2], cities=entry[3])
        actual_result.append(result)
    assert actual_result == expected_result
