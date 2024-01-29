import os
from pathlib import Path

import toml

from pyinit.res import Resources


class Project:
    _path: Path
    _res: Resources

    def __init__(self, path: Path, res: Resources) -> None:
        self._path = path
        self._res = res
        self._module_name = self._extract_module_name(self.path.name)

    @property
    def module_name(self):
        return self._module_name

    @property
    def path(self):
        return self._path

    @property
    def tests_path(self):
        return self.path / "tests"

    @property
    def src_path(self):
        return self.path / "src"

    @property
    def module_path(self):
        return self.src_path / self.module_name

    def _create_dirs(self):
        if not self.path.exists():
            self.path.mkdir()

        self.src_path.mkdir()
        self.module_path.mkdir()
        (self.module_path / "cli.py").write_bytes(self._res.script.read_bytes())
        (self.path / ".gitignore").write_bytes(self._res.gitignore.read_bytes())

        pyproject = toml.loads(self._res.pyproject.read_text())
        pyproject["project"]["name"] = self.module_name
        pyproject["project"]["scripts"] = {
            self.module_name: f"{self.module_name}.cli:main"
        }

        pyproject["project"]["authors"] = [
            {"name": "John Doe", "email": "jdoe@email.com"}
        ]
        (self.path / "pyproject.toml").write_text(toml.dumps(pyproject))

        self.tests_path.mkdir()

    def initialize(self) -> None:
        self._create_dirs()

    @staticmethod
    def _extract_module_name(name: str) -> str:
        # remove leading and trailing non-aplha chars
        while len(name) > 0:
            if not name[0].isalpha():
                name = name[1:]
                continue

            if not name[-1].isalnum():
                name = name[:-1]
                continue

            break

        # replace dashes with underscores
        name = name.replace("-", "_")

        # remove symbols
        name = "".join(filter(lambda c: c.isalpha() or c.isdigit() or c == "_", name))
        return name.lower()
