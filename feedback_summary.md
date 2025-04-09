# Feedback Summary Module

## Overview
The `feedback_summary.py` script provides functions to summarize student feedback, including:
- Extracting top scores.
- Calculating grade-wise counts.

## Usage

### Functions
1. `get_top_scores(feedback_file, top_n=5)`
   - Extracts the top `N` scores from the feedback file.
   - **Arguments:**
     - `feedback_file` (str): Path to the feedback file.
     - `top_n` (int): Number of top scores to extract. Default is 5.
   - **Returns:** List of top scores.

2. `get_grade_wise_counts(feedback_file)`
   - Calculates the grade-wise count of feedback entries.
   - **Arguments:**
     - `feedback_file` (str): Path to the feedback file.
   - **Returns:** Dictionary with grades as keys and their counts as values.

## Example
Assume the feedback file `student_feedback.txt` contains:
```
John,90,A
Jane,85,B
Doe,95,A
Alice,88,B
Bob,70,C
```

### Extract Top Scores
```python
from src.feedback_summary import get_top_scores

top_scores = get_top_scores("student_feedback.txt", top_n=3)
print(top_scores)  # Output: [95, 90, 88]
```

### Grade-Wise Counts
```python
from src.feedback_summary import get_grade_wise_counts

grade_counts = get_grade_wise_counts("student_feedback.txt")
print(grade_counts)  # Output: {"A": 2, "B": 2, "C": 1}
```
