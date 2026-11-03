"""
Module: students.py
Description: Refactored and updated student data maintenance module.
Author: Solomon Azowenu (2024/A/SENG/0146)
Environment: Python 3.12+
"""

from typing import List, Dict, Any
import statistics
from pydantic import BaseModel, Field


class StudentModel(BaseModel):
    """Pydantic Schema for Adaptive Maintenance Data Validation."""
    name: str = Field(..., min_length=1, description="Student Name")
    score: float = Field(..., ge=0, le=100, description="Student Score (0-100)")


students: List[Dict[str, Any]] = [
    {"name": "James", "score": 45.0},
    {"name": "Deborah", "score": 82.0},
    {"name": "Solomon", "score": 95.0},
    {"name": "Chinedu", "score": 78.0}
]


def average_score(data: List[Dict[str, Any]]) -> float:
    """
    Corrective & Preventive Maintenance:
    Safely calculates average score and avoids ZeroDivisionError.
    """
    if not data:
        return 0.0
    total = sum(d["score"] for d in data)
    return total / len(data)


def median_score(data: List[Dict[str, Any]]) -> float:
    """
    Perfective Maintenance:
    Calculates median score across dataset.
    """
    if not data:
        return 0.0
    scores = [d["score"] for d in data]
    return float(statistics.median(scores))


def add_student(name: str, score: float) -> bool:
    """
    Adaptive Maintenance:
    Validates input using Pydantic schema before inserting.
    """
    try:
        validated = StudentModel(name=name, score=score)
        students.append(validated.model_dump())
        print(f"[SUCCESS] Added student: {validated.name} (Score: {validated.score})")
        return True
    except Exception as err:
        print(f"[VALIDATION ERROR] {err}")
        return False


def display_report() -> None:
    """
    Perfective Maintenance:
    Renders structured console output.
    """
    print("=" * 40)
    print(f"{'STUDENT NAME':<25} | {'SCORE':<10}")
    print("=" * 40)
    for student in students:
        print(f"{student['name']:<25} | {student['score']:<10.2f}")
    print("=" * 40)
    print(f"Average Score: {average_score(students):.2f}")
    print(f"Median Score:  {median_score(students):.2f}")
    print("=" * 40)


if __name__ == "__main__":
    display_report()
    add_student("Amina", 89.5)
    display_report()