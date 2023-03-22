import pytest
from unittest_proj.utils.dicts import get_val


@pytest.fixture
def function_1():
    return {"vcs": "mercurial"}, {}

def tester_get_val(function_1):
    function_2, function_3 = function_1
    assert get_val(function_2, "vcs") == "mercurial"
    assert get_val(function_2, "vcs", "git") == "mercurial"
    assert get_val(function_2, "", "git") == "git"
    assert get_val(function_2, "git") == "git"
    assert get_val(function_3, "vcs") == "git"
    assert get_val(function_3, "vcs", "bazaar") == "bazaar"