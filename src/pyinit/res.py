import importlib.resources
from importlib.resources.abc import Traversable


class Resources:
    _script: Traversable

    def __init__(self) -> None:
        t = importlib.resources.files("pyinit.resources")
        self._script = t.joinpath("hello_world.py")
        self._gitignore = t / ".gitignore"
        self._pyproject = t / "pyproject.toml"

    @property
    def script(self) -> Traversable:
        return self._script

    @property
    def gitignore(self) -> Traversable:
        return self._gitignore

    @property
    def pyproject(self) -> Traversable:
        return self._pyproject
