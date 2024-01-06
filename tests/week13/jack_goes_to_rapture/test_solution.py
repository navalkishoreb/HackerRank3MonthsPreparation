import pytest

from src.week13.jack_goes_to_rapture.solution import get_cost


@pytest.mark.parametrize(argnames="case_no,", argvalues=["15"])
@pytest.mark.timeout(10)
def test_testcases(case_no):
    input_file = f"resources/input/input{case_no}.txt"
    expected_file = f"resources/output/output{case_no}.txt"

    with open(input_file) as input_stream:
        g_nodes, g_edges = list(map(int, next(input_stream).strip().split()))
        g_from = [0] * g_edges
        g_to = [0] * g_edges
        g_weight = [0] * g_edges

        for i in range(g_edges):
            g_from[i], g_to[i], g_weight[i] = list(map(int, next(input_stream).strip().split()))

    with open(expected_file) as input_stream:
        value = next(input_stream).strip()
        try:
            expected_result = int(value)
        except ValueError:
            expected_result = value

    actual_result = get_cost(g_nodes=g_nodes, g_from=g_from, g_to=g_to, g_weight=g_weight)

    assert actual_result == expected_result

#
# if __name__ == "__main__":
#     test_testcases(case_no="01")
