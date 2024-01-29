from pathlib import Path
from unittest.mock import Mock

import pytest

from pyinit.project import Project
from pyinit.res import Resources


class MockPath(Mock, Path):
    pass


@pytest.mark.parametrize(
    "path,expected_module_name",
    [
        (Path("/home/a-b-c-d"), "a_b_c_d"),
        (Path("/home/asdf/asdf/ABC"), "abc"),
        (Path("/AbC-123_"), "abc_123"),
        (Path("/asdf/123abc"), "abc"),
    ],
)
def test_module_name(path: MockPath, expected_module_name: str):
    project = Project(path, Resources())
    assert project.module_name == expected_module_name


def test_initialize(tmp_path: Mock):
    project_path = tmp_path / "my-project"
    project = Project(project_path, Resources())

    assert not project.src_path.exists()
    assert not project.module_path.exists()
    assert not project.tests_path.exists()

    project.initialize()

    assert project.src_path.exists()
    assert project.module_path.exists()
    assert project.tests_path.exists()
