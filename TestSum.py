import pytest
from sum import sum


def test_sum_with_int_works():
    assert (10 + 12) == sum(10, 12)


def test_sum_with_str_works():
    assert ("ab" + "cd") == sum("ab", "cd")