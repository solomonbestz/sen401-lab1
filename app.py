"""
Main Application Entry Point
Demonstrates baseline execution.
"""
from students import students
from utils.helpers import get_highest_score, get_lowest_score

def main():
    print("--- SEN 401 Baseline Application v1.0 ---")
    print(f"Total Students Registered: {len(students)}")
    
    highest = get_highest_score(students)
    lowest = get_lowest_score(students)
    
    if highest:
        print(f"Highest Scorer: {highest['name']} ({highest['score']})")
    if lowest:
        print(f"Lowest Scorer: {lowest['name']} ({lowest['score']})")

if __name__ == "__main__":
    main()