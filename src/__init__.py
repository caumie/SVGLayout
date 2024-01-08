import os
from pathlib import Path
from xml.etree import ElementTree as ET


class SVGLayout:
    def __init__(self) -> None:
        print(self)
        pass


class SvgFileLoader:
    def __init__(self, path: str) -> None:
        self.path = Path(path)
        if not self.path.exists():
            raise FileNotFoundError(self.path)
        f = str(self.path.resolve())
        self.tree = ET.parse(f)
