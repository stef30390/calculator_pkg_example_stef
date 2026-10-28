from pathlib import Path
import time
from ..calculator import Calculator

from tqdm import tqdm

class FileCalculator(Calculator):
    def __init__(self, path: Path =Path(__file__).parent / "nums.csv", expected_lines: int =3) -> None:
        self.path:Path = path
        self.expected_lines: int = 3
    def add_file(self) -> float:
        total:float  = 0
        with open(self.path) as f:
            for line in tqdm(f, total=self.expected_lines, desc="Adding numbers from file"):
                time.sleep(2)
                total = float(line)
                
        return total