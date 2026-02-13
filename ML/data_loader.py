"""
This file load raw data frm disk and return clean Python objects for structured ML pipeline.
"""
from problem import Problem
import json
from pathlib import Path

class DataLoader:
    def __init__(self, data_root: str):
        self.data_root = Path(data_root)

    def exists(self) -> bool:
        return self.data_root.exists()

    def list_files(self):
        if not self.exists():
            raise FileNotFoundError(f"Data directory not found: {self.data_root}")

        return [file for file in self.data_root.iterdir() if file.is_file()]
    
    def load_json(self, file_path: Path) -> dict:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def load_problem(self, file_path:Path) -> Problem:
        data = self.load_json(file_path)

        return Problem(
            id=data["id"],
            title=data["title"],
            difficulty=data["difficulty"],
            source=data["source"],
            skills=data["skills"],
            problem=data["problem"],
            expected_approach=data["expected_approach"],
            common_mistakes=data["common_mistakes"],
        )
